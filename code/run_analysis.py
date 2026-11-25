import numpy as np, pandas as pd, warnings
from scipy import stats
from scipy.optimize import linprog
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
P = '/tmp/claude-0/-home-claude/5ed52829-823d-5802-846d-3e50f577c3a4/scratchpad/panel/'
OUT = '/tmp/claude-0/-home-claude/5ed52829-823d-5802-846d-3e50f577c3a4/scratchpad/analysis/'
W = pd.read_csv(P + 'country_panel_wide.csv').set_index('economy')
L = pd.read_csv(P + 'country_panel_long.csv')
rng = np.random.default_rng(42)
R = []  # report sections: (title, text or DataFrame)
def sec(title, obj=None, note=None):
    R.append((title, obj, note))
def fmt(df, d=3):
    return df.round(d).to_markdown() if hasattr(df, 'to_markdown') else str(df)

# ---------- OLS with HC3 / cluster-robust SEs ----------
def ols(y, X, cols, cluster=None):
    y = np.asarray(y, float); X = np.asarray(X, float)
    X = np.column_stack([np.ones(len(y)), X]); names = ['const'] + list(cols)
    XtXi = np.linalg.inv(X.T @ X); b = XtXi @ X.T @ y; e = y - X @ b
    n, k = X.shape
    if cluster is None:
        H = np.einsum('ij,jk,ik->i', X, XtXi, X)
        w = e**2 / (1 - H)**2
        V = XtXi @ (X.T * w) @ X @ XtXi; df = n - k
    else:
        g = pd.factorize(np.asarray(cluster))[0]; G = g.max() + 1
        meat = np.zeros((k, k))
        for j in range(G):
            s = X[g == j].T @ e[g == j]; meat += np.outer(s, s)
        V = XtXi @ meat @ XtXi * G / (G - 1) * (n - 1) / (n - k); df = G - 1
    se = np.sqrt(np.diag(V)); t = b / se; p = 2 * stats.t.sf(np.abs(t), df)
    sse = e @ e; sst = ((y - y.mean())**2).sum(); r2 = 1 - sse / sst
    adj = 1 - (1 - r2) * (n - 1) / (n - k)
    vif = {}
    if len(cols) > 1:
        for j, c in enumerate(cols, start=1):
            others = np.delete(X[:, 1:], j - 1, axis=1)
            Z = np.column_stack([np.ones(n), others]); bb = np.linalg.lstsq(Z, X[:, j], rcond=None)[0]
            rr = X[:, j] - Z @ bb; r2j = 1 - rr @ rr / ((X[:, j] - X[:, j].mean())**2).sum()
            vif[c] = 1 / (1 - r2j)
    tab = pd.DataFrame({'coef': b, 'se': se, 'p': p}, index=names)
    tab['ci_low'] = b - stats.t.ppf(.975, df) * se; tab['ci_high'] = b + stats.t.ppf(.975, df) * se
    return dict(tab=tab, n=n, r2=r2, adj=adj, V=V, b=b, names=names, vif=vif, resid=e, X=X, df=df)
def model_row(name, res):
    t = res['tab'].loc[[c for c in res['names'] if c != 'const']]
    return t.assign(model=name)
def summarize(name, res):
    return f"{name}: N={res['n']}, R2={res['r2']:.3f}, adj R2={res['adj']:.3f}"

# ---------- 0. Sample and descriptives ----------
core_all = ['perf2','jobs8','perf3','perf1','bready_wk1','wk2','t7','t9','t8','bready_t10','mgmt1','fin34','fin14','fin21','fin11','bready_fin27','car1','t3','survey_year']
desc = W[core_all].agg(['count','mean','std','median','min','max']).T
desc.to_csv(OUT + 'T1_descriptives.csv')
sec('1. Descriptive statistics (economy level, all firms)', desc)
top = {}
for v in ['perf2','bready_wk1','t7','mgmt1']:
    s = W[v].dropna().sort_values()
    top[v] = pd.DataFrame({'bottom_5': list(s.head(5).index) + [''] * 0, 'top_5': list(s.tail(5).index[::-1])}, index=range(5))
    top[v] = pd.DataFrame({'Highest 5': [f"{i} ({W.loc[i, v]:.1f})" for i in s.tail(5).index[::-1]],
                           'Lowest 5': [f"{i} ({W.loc[i, v]:.1f})" for i in s.head(5).index]})
    top[v].to_csv(OUT + f'T2_top_bottom_{v}.csv', index=False)
sec('2. Highest and lowest economies (value in brackets)', '\n\n'.join(f"**{v}**\n\n" + fmt(top[v], 1) for v in top))

# ---------- 1. Correlations ----------
cvars = ['perf2','jobs8','perf3','bready_wk1','wk2','t7','t9','bready_t10','mgmt1','fin34','car1','survey_year']
pear = W[cvars].corr(method='pearson', min_periods=30); spear = W[cvars].corr(method='spearman', min_periods=30)
pear.to_csv(OUT + 'T3_pearson.csv'); spear.to_csv(OUT + 'T3_spearman.csv')
rows = []
for y in ['perf2','jobs8']:
    for x in ['bready_wk1','wk2','t7','t9','bready_t10','mgmt1']:
        d = W[[y, x]].dropna(); r, p = stats.pearsonr(d[x], d[y]); rs, ps = stats.spearmanr(d[x], d[y])
        rows.append(dict(outcome=y, predictor=x, N=len(d), pearson_r=r, p_pearson=p, spearman_rho=rs, p_spearman=ps))
bivar = pd.DataFrame(rows); bivar.to_csv(OUT + 'T4_bivariate.csv', index=False)
sec('3. Bivariate correlations with employment growth and net job creation', bivar)
# Fisher z tests of correlation by size group (from long data)
Lp = L.pivot_table(index=['economy','segment'], columns='indicator_code', values='value', aggfunc='first').reset_index()
sec('4. Correlation matrix (Pearson, economy level)', pear)
# heatmap
fig, ax = plt.subplots(figsize=(9, 8))
im = ax.imshow(pear.values, cmap='RdBu_r', vmin=-1, vmax=1)
ax.set_xticks(range(len(cvars))); ax.set_xticklabels(cvars, rotation=45, ha='right'); ax.set_yticks(range(len(cvars))); ax.set_yticklabels(cvars)
for i in range(len(cvars)):
    for j in range(len(cvars)):
        v = pear.values[i, j]
        if not np.isnan(v): ax.text(j, i, f"{v:.2f}", ha='center', va='center', fontsize=6)
plt.colorbar(im); plt.title('Pearson correlations (economy level)'); plt.tight_layout(); plt.savefig(OUT + 'F1_correlation_heatmap.png', dpi=130); plt.close()
# scatter
fig, axs = plt.subplots(1, 3, figsize=(13, 4))
for ax, x in zip(axs, ['bready_wk1','t7','mgmt1']):
    d = W[['perf2', x]].dropna(); ax.scatter(d[x], d['perf2'], s=14, alpha=.6)
    m, c = np.polyfit(d[x], d['perf2'], 1); xs = np.linspace(d[x].min(), d[x].max(), 50); ax.plot(xs, m * xs + c, 'r')
    ax.set_xlabel(x); ax.set_ylabel('perf2: employment growth (%)'); ax.set_title(f"{x} vs employment growth (N={len(d)})")
plt.tight_layout(); plt.savefig(OUT + 'F2_scatter.png', dpi=130); plt.close()

# ---------- 2. Management index ----------
mg = W[['mgmt2','mgmt3','mgmt4','mgmt5','mgmt6']].dropna()
k = mg.shape[1]; alpha = k / (k - 1) * (1 - mg.var().sum() / mg.sum(axis=1).var())
pca = PCA(n_components=1).fit((mg - mg.mean()) / mg.std())
score = pd.Series(pca.transform((mg - mg.mean()) / mg.std())[:, 0], index=mg.index)
r_pc_m1 = stats.pearsonr(score.loc[W.dropna(subset=['mgmt1']).index.intersection(score.index)], W.loc[W.dropna(subset=['mgmt1']).index.intersection(score.index), 'mgmt1'])[0]
sec('5. Management index check', f"Cronbach's alpha for mgmt2-mgmt6 (N={len(mg)}): {alpha:.3f}. PCA first component explains {pca.explained_variance_ratio_[0]*100:.1f}% of variance. Correlation of PCA score with mgmt1: {r_pc_m1:.3f}. Main models use mgmt1 (the reported index).")

# ---------- 3. Group comparisons (paired within economy) ----------
def pair(code, a, b):
    s = Lp[['economy', 'segment', code]].dropna() if code in Lp.columns else None
    if s is None: return None
    pv = s.pivot_table(index='economy', columns='segment', values=code, aggfunc='first')
    if a not in pv or b not in pv: return None
    d = pv[[a, b]].dropna()
    if len(d) < 8: return dict(comparison=f"{a} vs {b}", indicator=code, N=len(d), mean_a=np.nan, mean_b=np.nan, diff=np.nan, p_t=np.nan, p_wilcoxon=np.nan)
    t = stats.ttest_rel(d[a], d[b]); w = stats.wilcoxon(d[a], d[b])
    return dict(comparison=f"{a} vs {b}", indicator=code, N=len(d), mean_a=d[a].mean(), mean_b=d[b].mean(), diff=(d[a]-d[b]).mean(), p_t=t.pvalue, p_wilcoxon=w.pvalue)
comps = []
for code in ['perf2','perf3','bready_wk1','wk2','t7','t9','bready_t10','mgmt1']:
    for a, b in [('Small (5-19)','Large (100+)'), ('Medium (20-99)','Large (100+)'), ('Small (5-19)','Medium (20-99)'),
                 ('Direct exports are 10% or more of sales','Non-exporter'), ('10% or more foreign ownership','Domestic'),
                 ('Top manager is female','Top manager is male'), ('Manufacturing (All)','Services (All)')]:
        r = pair(code, a, b)
        if r: comps.append(r)
comps = pd.DataFrame(comps); comps.to_csv(OUT + 'T5_group_comparisons.csv', index=False)
sec('6. Group comparisons within economy (paired tests; rows with N<8 are omitted)', comps)

# Friedman across sizes
tri = Lp.pivot_table(index='economy', columns='segment', values='perf2', aggfunc='first')[['Small (5-19)','Medium (20-99)','Large (100+)']].dropna()
fr = stats.friedmanchisquare(tri.iloc[:,0], tri.iloc[:,1], tri.iloc[:,2])
sec('7. Friedman test: employment growth across size groups', f"N={len(tri)} economies with all three size groups. chi2={fr.statistic:.2f}, p={fr.pvalue:.4f}. Mean growth: Small {tri.iloc[:,0].mean():.2f}, Medium {tri.iloc[:,1].mean():.2f}, Large {tri.iloc[:,2].mean():.2f}.")

# ---------- 4. Main multivariate models ----------
def mdl(y, xs, data, controls=('survey_year',)):
    cols = list(xs) + list(controls)
    d = data[[y] + cols].dropna()
    return ols(d[y].values, d[cols].values, cols), d
m1, d1 = mdl('perf2', ['bready_wk1','t7','mgmt1','fin34'], W)
# standardized
Z = W.copy()
for c in ['perf2','bready_wk1','t7','mgmt1','fin34','survey_year']: Z[c] = (W[c] - W[c].mean()) / W[c].std()
m1z, _ = mdl('perf2', ['bready_wk1','t7','mgmt1','fin34'], Z)
m2, d2 = mdl('perf2', ['bready_wk1','t7','mgmt1','fin34','int_tr_inn','int_mg_inn'], W.assign(int_tr_inn=W.bready_wk1*W.t7, int_mg_inn=W.mgmt1*W.t7))
W2 = W.copy(); W2['bready_x_fin'] = W2.bready_wk1*W2.fin34; W2['t7_x_fin'] = W2.t7*W2.fin34; W2['mgmt_x_fin'] = W2.mgmt1*W2.fin34
m3, d3 = mdl('perf2', ['bready_wk1','t7','mgmt1','fin34','bready_x_fin','t7_x_fin','mgmt_x_fin'], W2)
m4, _ = mdl('jobs8', ['bready_wk1','t7','mgmt1','fin34'], W)
m5, _ = mdl('perf3', ['bready_wk1','t7','mgmt1','fin34'], W)
m6, _ = mdl('perf2', ['wk2','t7','mgmt1','fin34'], W)
m7, _ = mdl('perf2', ['bready_wk1','t7','fin34'], W)
main = pd.concat([model_row('M1 perf2 baseline (raw)', m1), model_row('M2 perf2 + training x innovation, mgmt x innovation', m2),
                  model_row('M3 perf2 + credit interactions', m3), model_row('M4 DV jobs8 (net job creation)', m4),
                  model_row('M5 DV perf3 (labour productivity growth)', m5), model_row('M6 non-B-READY training (wk2)', m6),
                  model_row('M7 perf2 without management (N larger)', m7)])
main.to_csv(OUT + 'T6_main_models.csv')
sec('8. Main multivariate models (economy level, HC3 robust SEs)',
    '\n\n'.join(summarize(n, r) for n, r in [('M1', m1), ('M2', m2), ('M3', m3), ('M4 jobs8', m4), ('M5 perf3', m5), ('M6 wk2', m6), ('M7', m7)]) + '\n\n' +
    fmt(main, 3))
sec('9. Standardised coefficients, M1 (z-scored; effect of 1 SD change)', fmt(model_row('M1 std', m1z), 3))
sec('10. Multicollinearity (VIF), M1 and M2', f"M1 VIF: {', '.join(f'{k} {v:.2f}' for k,v in m1['vif'].items())}. M2 VIF: {', '.join(f'{k} {v:.2f}' for k,v in m2['vif'].items())}. Flag >5.")

# ---------- 5. Stacked firm-size model ----------
S = L[(L.segment.isin(['Small (5-19)','Medium (20-99)','Large (100+)'])) & (L.indicator_code.isin(['perf2','bready_wk1','t7']))]
sp = S.pivot_table(index=['economy','segment'], columns='indicator_code', values='value', aggfunc='first').reset_index().dropna()
sp['med'] = (sp.segment == 'Medium (20-99)').astype(float); sp['lrg'] = (sp.segment == 'Large (100+)').astype(float)
sp['tr_med'] = sp.bready_wk1*sp.med; sp['tr_lrg'] = sp.bready_wk1*sp.lrg
sp['in_med'] = sp.t7*sp.med; sp['in_lrg'] = sp.t7*sp.lrg
xs = ['bready_wk1','t7','med','lrg','tr_med','tr_lrg','in_med','in_lrg']
ms = ols(sp.perf2.values, sp[xs].values, xs, cluster=sp.economy.values)
# Wald test on interactions
idx = [ms['names'].index(c) for c in ['tr_med','tr_lrg','in_med','in_lrg']]
Vi = ms['V'][np.ix_(idx, idx)]; bi = ms['b'][idx]
wald = bi @ np.linalg.inv(Vi) @ bi; pw = stats.chi2.sf(wald, len(idx))
sec('11. Stacked firm-size model: employment growth on training and innovation by size (economy-clustered SEs)',
    f"Stacked observations: {len(sp)} (economy x size); clusters: {sp.economy.nunique()}. Wald test that size interactions are all zero: chi2({len(idx)})={wald:.2f}, p={pw:.4f}.\n\n" + fmt(ms['tab'], 3))

# ---------- 6. Mediation: management -> innovation -> employment growth ----------
md = W[['mgmt1','t7','perf2']].dropna()
def med_est(d):
    a = ols(d.t7.values, d[['mgmt1']].values, ['mgmt1'])['b'][1]
    bres = ols(d.perf2.values, d[['t7','mgmt1']].values, ['t7','mgmt1'])['b']
    return a * bres[1], a, bres[1], bres[2]
ind, a, b, cdir = med_est(md)
B = 5000; boots = []
for _ in range(B):
    s = md.sample(len(md), replace=True, random_state=rng.integers(1e9))
    boots.append(med_est(s)[0])
lo, hi = np.percentile(boots, [2.5, 97.5])
sec('12. Mediation: management -> innovation -> employment growth (bootstrap, 5,000 draws)',
    f"N={len(md)}. a path (mgmt1 -> t7) = {a:.3f}; b path (t7 -> perf2 controlling mgmt1) = {b:.3f}; direct effect of mgmt1 on perf2 = {cdir:.3f}. Indirect effect = {ind:.3f}, bootstrap 95% CI [{lo:.3f}, {hi:.3f}]. " +
    ('Indirect effect excludes zero.' if (lo > 0 or hi < 0) else 'Indirect effect includes zero.') + " Cross-sectional: this tests a hypothesised path, not causal order.")

# ---------- 7. Moderation: innovation x credit constraint ----------
mo = W[['perf2','t7','fin34','survey_year']].dropna().copy()
mo['t7z'] = (mo.t7 - mo.t7.mean())/mo.t7.std(); mo['finz'] = (mo.fin34 - mo.fin34.mean())/mo.fin34.std()
mo['int'] = mo.t7z*mo.finz
mm = ols(mo.perf2.values, mo[['t7z','finz','int','survey_year']].values, ['t7z','finz','int','survey_year'])
rows = []
for lvl, lab in [(-1,'-1 SD credit constraint'),(0,'mean'),(1,'+1 SD credit constraint')]:
    bsl = mm['b'][1] + mm['b'][3]*lvl
    vsl = mm['V'][1,1] + lvl**2*mm['V'][3,3] + 2*lvl*mm['V'][1,3]
    t = bsl/np.sqrt(vsl); p = 2*stats.t.sf(abs(t), mm['df'])
    rows.append(dict(level=lab, slope_t7_on_perf2=bsl, se=np.sqrt(vsl), p=p))
sec('13. Moderation: does credit constraint weaken innovation -> employment growth? (simple slopes)',
    f"N={len(mo)}. Interaction coefficient = {mm['b'][3]:.3f} (p={mm['tab'].p.iloc[3]:.4f}).\n\n" + fmt(pd.DataFrame(rows), 3))

# ---------- 8. Robustness ----------
def qr(y, X, tau):
    n, k = X.shape
    c = np.concatenate([np.zeros(k), tau*np.ones(n), (1-tau)*np.ones(n)])
    Aeq = np.hstack([X, np.eye(n), -np.eye(n)])
    bounds = [(None, None)]*k + [(0, None)]*(2*n)
    r = linprog(c, A_eq=Aeq, b_eq=y, bounds=bounds, method='highs')
    return r.x[:k]
qd = W[['perf2','bready_wk1','t7','mgmt1','fin34','survey_year']].dropna()
Xq = np.column_stack([np.ones(len(qd)), qd[['bready_wk1','t7','mgmt1','fin34','survey_year']].values])
qrows = {}
for tau in [0.25, 0.5, 0.75]:
    qrows[f"q{int(tau*100)}"] = qr(qd.perf2.values, Xq, tau)
qtab = pd.DataFrame(qrows, index=['const','bready_wk1','t7','mgmt1','fin34','survey_year'])
qtab.to_csv(OUT + 'T7_quantile.csv')
sec('14. Quantile regression of employment growth (M1 specification)', f"N={len(qd)}.\n\n" + fmt(qtab, 3))

# Huber robust regression (IRLS)
def huber(y, X, c=1.345, it=100):
    b = np.linalg.lstsq(X, y, rcond=None)[0]
    for _ in range(it):
        r = y - X@b; s = np.median(np.abs(r - np.median(r)))/0.6745
        u = np.abs(r)/s; w = np.where(u <= c, 1, c/u)
        b_new = np.linalg.lstsq(X*np.sqrt(w)[:,None], y*np.sqrt(w), rcond=None)[0]
        if np.allclose(b_new, b, atol=1e-8): break
        b = b_new
    return b
hb = huber(qd.perf2.values, Xq)
ols_b = ols(qd.perf2.values, qd[['bready_wk1','t7','mgmt1','fin34','survey_year']].values, ['bready_wk1','t7','mgmt1','fin34','survey_year'])['b']
# Cook's distance & influence for M1
cook = (m1['resid']**2/( (m1['X'].shape[1]) * (m1['resid']@m1['resid'])/(m1['n']-m1['X'].shape[1]) )) * (np.einsum('ij,jk,ik->i', m1['X'], np.linalg.inv(m1['X'].T@m1['X']), m1['X']))/(1-np.einsum('ij,jk,ik->i', m1['X'], np.linalg.inv(m1['X'].T@m1['X']), m1['X']))**2
cook = pd.Series(cook, index=d1.index).sort_values(ascending=False)
sec('15. Robustness: Huber regression and influence (M1 specification)',
    fmt(pd.DataFrame({'OLS': ols_b, 'Huber': hb}, index=['const','bready_wk1','t7','mgmt1','fin34','survey_year']), 3) +
    f"\n\nMost influential economies (Cook's D, top 5): " + ', '.join(f"{i} ({v:.2f})" for i, v in cook.head(5).items()) +
    f". Rule of thumb threshold 4/N = {4/len(d1):.3f}; economies above it: {int((cook > 4/len(d1)).sum())}.")
# Drop non-B-READY / alternative specs done as M6, M7; jackknife of key coefficient
jk = []
for econ in d1.index:
    dd = d1.drop(econ)
    rr = ols(dd.perf2.values, dd[['bready_wk1','t7','mgmt1','fin34','survey_year']].values, ['bready_wk1','t7','mgmt1','fin34','survey_year'])
    jk.append(rr['b'][1:4])
jk = np.array(jk)
sec('16. Leave-one-economy-out stability (coefficients on training, innovation, management)',
    f"Ranges across {len(d1)} re-estimates: training [{jk[:,0].min():.3f}, {jk[:,0].max():.3f}], innovation [{jk[:,1].min():.3f}, {jk[:,1].max():.3f}], management [{jk[:,2].min():.3f}, {jk[:,2].max():.3f}]. Full-sample: training {m1['b'][1]:.3f}, innovation {m1['b'][2]:.3f}, management {m1['b'][3]:.3f}.")

# ---------- 9. Clustering ----------
cl = W[['bready_wk1','t7','mgmt1','fin34']].dropna()
zc = (cl - cl.mean())/cl.std()
sil = {}
for kk in range(2, 7):
    km = KMeans(n_clusters=kk, n_init=20, random_state=42).fit(zc.values)
    sil[kk] = silhouette_score(zc.values, km.labels_)
best = max(sil, key=sil.get)
km = KMeans(n_clusters=best, n_init=20, random_state=42).fit(zc.values)
cl = cl.assign(cluster=km.labels_).join(W[['perf2','perf3','jobs8']])
cprof = cl.groupby('cluster').agg(N=('perf2','size'), training=('bready_wk1','mean'), innovation=('t7','mean'), mgmt=('mgmt1','mean'), credit_constr=('fin34','mean'), emp_growth=('perf2','mean'), prod_growth=('perf3','mean'), net_job_creation=('jobs8','mean'))
cprof.to_csv(OUT + 'T8_clusters.csv')
sec('17. Economy clusters (k-means on training, innovation, management, credit constraint)',
    'Silhouette by k: ' + ', '.join(f"k={k}: {v:.3f}" for k, v in sil.items()) + f". Chosen k={best}.\n\n" + fmt(cprof, 2))

# ---------- 10. Convergence: large vs small productivity gap ----------
cv = Lp.pivot_table(index='economy', columns='segment', values='perf3', aggfunc='first')[['Small (5-19)','Large (100+)']].dropna()
cv['gap'] = cv['Large (100+)'] - cv['Small (5-19)']
cres = ols(cv.gap.values, cv[['Small (5-19)']].values, ['Small (5-19)'])
sec('18. Size productivity gap (Large minus Small labour productivity growth) and convergence check',
    f"N={len(cv)}. Mean gap = {cv.gap.mean():.3f} (t-test p={stats.ttest_1samp(cv.gap, 0).pvalue:.4f}). Regression of gap on Small-firm productivity growth: slope = {cres['b'][1]:.3f} (p={cres['tab'].p.iloc[1]:.4f}). A negative slope means the gap narrows where small firms grow faster.")

# ---------- 11. Regional descriptives (from aggregates) ----------
agg = pd.read_csv(P + 'country_panel_long.csv')  # aggregates were excluded from panel; reload raw
raw = pd.read_csv(P + 'long_raw.csv', keep_default_na=False, dtype=str)
reg = ['East Asia & Pacific','Europe & Central Asia','Latin America & Caribbean','North America','South Asia','Sub-Saharan Africa','All Economies']
ra = raw[(raw.year == '') & (raw.place.isin(reg)) & (raw.segment == 'All') & (raw.indicator_code.isin(['perf2','bready_wk1','t7','mgmt1','fin34']))]
ra = ra.assign(value=pd.to_numeric(ra.value_raw, errors='coerce')).drop_duplicates(['indicator_code','place'])
rt = ra.pivot_table(index='place', columns='indicator_code', values='value', aggfunc='first').reindex(reg)
rt.to_csv(OUT + 'T9_regional.csv')
sec('19. Regional aggregates (as published by the source; descriptive only)', fmt(rt, 2))

# ---------- Assemble report ----------
out = ['# Analysis results: Building Productive Firms', '', 'Sample: 181 economies, one survey year each (2009 to 2026). Cross-sectional: results are correlations between economies, not causal effects over time.', '']
for title, obj, note in R:
    out.append(f'## {title}'); out.append('')
    if obj is not None:
        out.append(obj.to_markdown(floatfmt='.3f') if isinstance(obj, pd.DataFrame) else str(obj))
    if note: out.append(note)
    out.append('')
open(OUT + 'analysis_results.md', 'w').write('\n'.join(out))
print('done; sections:', len(R))
print('M1', summarize('M1', m1), 'coef', m1['tab'].round(3).to_string())

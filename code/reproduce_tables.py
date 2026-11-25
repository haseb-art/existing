"""Reproduce the regression tables in the paper (Tables 2, 2b, 3, 4, 5, 6 and the mediation estimates).

Requires: numpy, pandas, scipy, scikit-learn.
Run after build_income.py. Writes CSV outputs to results/.
"""
import numpy as np, pandas as pd
from pathlib import Path
from scipy import stats
from scipy.optimize import linprog
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results"; OUT.mkdir(exist_ok=True)
W = pd.read_csv(ROOT / "data" / "panel_income_survey.csv").set_index("economy")
L = pd.read_csv(ROOT / "data" / "country_panel_long.csv")

def ols(y, X, cols, cluster=None):
    """OLS with HC3 robust SEs, or cluster-robust SEs when cluster labels are given."""
    X = np.column_stack([np.ones(len(y)), X]); names = ["const"] + cols
    XtXi = np.linalg.inv(X.T @ X); b = XtXi @ X.T @ y; e = y - X @ b; n, k = X.shape
    if cluster is None:
        H = np.einsum("ij,jk,ik->i", X, XtXi, X)
        V = XtXi @ (X.T * (e**2 / (1 - H)**2)) @ X @ XtXi; df = n - k
    else:
        g = pd.factorize(np.asarray(cluster))[0]; G = g.max() + 1
        meat = np.zeros((k, k))
        for j in range(G):
            s = X[g == j].T @ e[g == j]; meat += np.outer(s, s)
        V = XtXi @ meat @ XtXi * G / (G - 1) * (n - 1) / (n - k); df = G - 1
    se = np.sqrt(np.diag(V)); p = 2 * stats.t.sf(np.abs(b / se), df)
    r2 = 1 - e @ e / ((y - y.mean())**2).sum()
    tab = pd.DataFrame({"coef": b, "se": se, "p": p}, index=names)
    return tab, n, r2, V, b

def run(dv, xs, data):
    d = data[[dv] + xs].dropna()
    tab, n, r2, _, _ = ols(d[dv].values, d[xs].values, xs)
    return tab, n, r2

CAP = ["bready_wk1", "t7", "mgmt1", "fin34"]
rows = []
# Table 2: ten-year mean income (main) and models without income
for label, dv, cap, inc in [
    ("A. Without income, employment growth", "perf2", CAP, None),
    ("B. Main model, employment growth", "perf2", CAP, "lgdppc_mean"),
    ("C. Net job creation", "jobs8", CAP, "lgdppc_mean"),
    ("D. Productivity growth", "perf3", CAP, "lgdppc_mean"),
    ("E. Workers trained (wk2), employment growth", "perf2", ["wk2", "t7", "mgmt1", "fin34"], "lgdppc_mean"),
    ("B'. Survey-year income, employment growth", "perf2", CAP, "lgdppc_survey"),
    ("C'. Survey-year income, net job creation", "jobs8", CAP, "lgdppc_survey"),
    ("D'. Survey-year income, productivity growth", "perf3", CAP, "lgdppc_survey"),
    ("E'. Survey-year income, workers trained", "perf2", ["wk2", "t7", "mgmt1", "fin34"], "lgdppc_survey"),
]:
    xs = cap + ["survey_year"] + ([inc] if inc else [])
    tab, n, r2 = run(dv, xs, W)
    rows.append({"model": label, "N": n, "R2": round(r2, 3), **{k: f"{tab.loc[k,'coef']:.3f} (p={tab.loc[k,'p']:.3f})" for k in tab.index if k != "const"}})
tab2 = pd.DataFrame(rows); tab2.to_csv(OUT / "table2_and_2b_models.csv", index=False)
print(tab2.to_string(), "\n")

# Table 3: quantile regression (main spec, ten-year income) and Huber regression
def qr(y, X, tau):
    n, k = X.shape; c = np.concatenate([np.zeros(k), tau * np.ones(n), (1 - tau) * np.ones(n)])
    A = np.hstack([X, np.eye(n), -np.eye(n)]); bnds = [(None, None)] * k + [(0, None)] * (2 * n)
    return linprog(c, A_eq=A, b_eq=y, bounds=bnds, method="highs").x[:k]
xs = CAP + ["survey_year", "lgdppc_mean"]
d = W[["perf2"] + xs].dropna(); X = np.column_stack([np.ones(len(d)), d[xs].values]); y = d.perf2.values
t3 = {f"quantile_{t}": qr(y, X, t) for t in [0.25, 0.5, 0.75]}
bh = np.linalg.lstsq(X, y, rcond=None)[0]
for _ in range(200):
    r = y - X @ bh; s = np.median(np.abs(r - np.median(r))) / 0.6745; u = np.abs(r) / s
    w = np.where(u <= 1.345, 1, 1.345 / u)
    bn = np.linalg.lstsq(X * np.sqrt(w)[:, None], y * np.sqrt(w), rcond=None)[0]
    if np.allclose(bn, bh, atol=1e-9): break
    bh = bn
t3["huber"] = bh
t3 = pd.DataFrame(t3, index=["const"] + xs).T
t3.to_csv(OUT / "table3_robustness.csv"); print(t3.round(3).to_string(), "\n")

# Table 4: paired within-economy comparisons
Lp = L.pivot_table(index=["economy", "segment"], columns="indicator_code", values="value", aggfunc="first").reset_index()
def paired(code, a, b):
    s = Lp[["economy", "segment", code]].dropna()
    pv = s.pivot_table(index="economy", columns="segment", values=code, aggfunc="first")
    if a not in pv or b not in pv: return None
    dd = pv[[a, b]].dropna()
    return dict(outcome=code, comparison=f"{a} vs {b}", N=len(dd), mean_first=dd[a].mean(), mean_second=dd[b].mean(),
                diff=(dd[a] - dd[b]).mean(), p_t=stats.ttest_rel(dd[a], dd[b]).pvalue,
                p_wilcoxon=stats.wilcoxon(dd[a], dd[b]).pvalue)
pairs = [("Small (5-19)", "Large (100+)"), ("Medium (20-99)", "Large (100+)"), ("Small (5-19)", "Medium (20-99)"),
         ("Direct exports are 10% or more of sales", "Non-exporter"), ("10% or more foreign ownership", "Domestic"),
         ("Top manager is female", "Top manager is male"), ("Manufacturing (All)", "Services (All)")]
t4 = pd.DataFrame([r for code in ["perf2", "perf3", "bready_wk1", "t7", "t9", "bready_t10", "mgmt1"]
                   for a, b in pairs if (r := paired(code, a, b))])
t4.to_csv(OUT / "table4_within_economy.csv", index=False)
print(t4[["outcome", "comparison", "N", "diff", "p_t", "p_wilcoxon"]].round(3).head(12).to_string(), "\n")

# Table 5: stacked firm-size model (no income control), clustered by economy
S = L[L.segment.isin(["Small (5-19)", "Medium (20-99)", "Large (100+)"]) & L.indicator_code.isin(["perf2", "bready_wk1", "t7"])]
sp = S.pivot_table(index=["economy", "segment"], columns="indicator_code", values="value", aggfunc="first").reset_index().dropna()
sp["med"] = (sp.segment == "Medium (20-99)").astype(float); sp["lrg"] = (sp.segment == "Large (100+)").astype(float)
sp["tr_med"] = sp.bready_wk1 * sp.med; sp["tr_lrg"] = sp.bready_wk1 * sp.lrg
sp["in_med"] = sp.t7 * sp.med; sp["in_lrg"] = sp.t7 * sp.lrg
xs5 = ["bready_wk1", "t7", "med", "lrg", "tr_med", "tr_lrg", "in_med", "in_lrg"]
tab5, n5, _, V5, b5 = ols(sp.perf2.values, sp[xs5].values, xs5, cluster=sp.economy.values)
idx = [xs5.index(c) + 1 for c in ["tr_med", "tr_lrg", "in_med", "in_lrg"]]
wald = b5[idx] @ np.linalg.inv(V5[np.ix_(idx, idx)]) @ b5[idx]
tab5.to_csv(OUT / "table5_stacked.csv")
print(tab5.round(3).to_string(), f"\nN obs={len(sp)} clusters={sp.economy.nunique()} Wald chi2(4)={wald:.2f} p={stats.chi2.sf(wald, 4):.4f}\n")

# Mediation: management -> innovation -> employment growth (income controlled), bootstrap 5000
md = W[["mgmt1", "t7", "perf2", "lgdppc_mean"]].dropna()
def med(dd):
    a = np.linalg.lstsq(np.column_stack([np.ones(len(dd)), dd.mgmt1, dd.lgdppc_mean]), dd.t7, rcond=None)[0][1]
    bb = np.linalg.lstsq(np.column_stack([np.ones(len(dd)), dd.t7, dd.mgmt1, dd.lgdppc_mean]), dd.perf2, rcond=None)[0]
    return a * bb[1], a, bb[1], bb[2]
rng = np.random.default_rng(42)
ind, a, bb1, direct = med(md)
boot = [med(md.sample(len(md), replace=True, random_state=int(rng.integers(1e9))))[0] for _ in range(5000)]
lo, hi = np.percentile(boot, [2.5, 97.5])
print(f"Mediation N={len(md)} a={a:.3f} b={bb1:.3f} direct={direct:.3f} indirect={ind:.3f} 95% CI [{lo:.3f}, {hi:.3f}]\n")

# Table 6: economy clusters (k-means, k=2 chosen by silhouette)
cl = W[["bready_wk1", "t7", "mgmt1", "fin34"]].dropna()
z = (cl - cl.mean()) / cl.std()
sil = {k: silhouette_score(z.values, KMeans(n_clusters=k, n_init=20, random_state=42).fit(z.values).labels_) for k in range(2, 7)}
km = KMeans(n_clusters=2, n_init=20, random_state=42).fit(z.values)
prof = cl.assign(cluster=km.labels_).join(W[["perf2", "perf3", "jobs8"]]).groupby("cluster").agg(
    N=("perf2", "size"), training=("bready_wk1", "mean"), innovation=("t7", "mean"), management=("mgmt1", "mean"),
    credit=("fin34", "mean"), emp_growth=("perf2", "mean"), prod_growth=("perf3", "mean"), net_job=("jobs8", "mean"))
prof.to_csv(OUT / "table6_clusters.csv")
print("silhouette:", {k: round(v, 3) for k, v in sil.items()}); print(prof.round(2).to_string())

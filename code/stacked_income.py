"""Stacked firm-size model with the income control (Table 5).
Economy x size rows; employment growth on training and innovation, size dummies,
their interactions and mean log GDP per capita; SEs clustered by economy;
joint Wald test of the four size interactions.
Reads data/country_panel_long.csv and data/panel_income_survey.csv; writes results/table5_stacked_with_income.csv."""
import numpy as np, pandas as pd
from scipy import stats

W = pd.read_csv('data/panel_income_survey.csv').set_index('economy')
L = pd.read_csv('data/country_panel_long.csv')
S = L[L.segment.isin(['Small (5-19)', 'Medium (20-99)', 'Large (100+)'])
      & L.indicator_code.isin(['perf2', 'bready_wk1', 't7'])]
sp = S.pivot_table(index=['economy', 'segment'], columns='indicator_code',
                   values='value', aggfunc='first').reset_index()
sp = sp.join(W[['lgdppc_mean']], on='economy').dropna()
sp['med'] = (sp.segment == 'Medium (20-99)').astype(float)
sp['lrg'] = (sp.segment == 'Large (100+)').astype(float)
sp['tr_med'] = sp.bready_wk1 * sp.med; sp['tr_lrg'] = sp.bready_wk1 * sp.lrg
sp['in_med'] = sp.t7 * sp.med;         sp['in_lrg'] = sp.t7 * sp.lrg
xs = ['bready_wk1', 't7', 'med', 'lrg', 'tr_med', 'tr_lrg', 'in_med', 'in_lrg', 'lgdppc_mean']
names = ['const'] + xs
X = np.column_stack([np.ones(len(sp)), sp[xs].values]); y = sp.perf2.values
XtXi = np.linalg.inv(X.T @ X); b = XtXi @ X.T @ y; e = y - X @ b
n, k = X.shape
g = pd.factorize(sp.economy.values)[0]; G = g.max() + 1
meat = np.zeros((k, k))
for j in range(G):
    s_ = X[g == j].T @ e[g == j]; meat += np.outer(s_, s_)
V = XtXi @ meat @ XtXi * G / (G - 1) * (n - 1) / (n - k)
se = np.sqrt(np.diag(V)); p = 2 * stats.t.sf(np.abs(b / se), G - 1)
out = pd.DataFrame({'term': names, 'coef': b, 'se': se, 'p': p}).round(4)
idx = [names.index(c) for c in ['tr_med', 'tr_lrg', 'in_med', 'in_lrg']]
w = b[idx] @ np.linalg.inv(V[np.ix_(idx, idx)]) @ b[idx]
print(out.to_string(index=False))
print(f'N = {n} observations, {G} economies; Wald chi2(4) = {w:.2f}, p = {stats.chi2.sf(w, 4):.4f}')
out.to_csv('results/table5_stacked_with_income.csv', index=False)

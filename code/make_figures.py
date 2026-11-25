"""Figures 3-5 for the paper. Figures 1-2 are produced by run_analysis.py (correlation heatmap, capability scatter).
Reads data/panel_income_survey.csv and results/table4_within_economy.csv and writes figures/*.png."""
import numpy as np, pandas as pd
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
ROOT = Path(__file__).resolve().parents[1]; FIG = ROOT / "figures"; FIG.mkdir(exist_ok=True)
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False})
W = pd.read_csv(ROOT / "data" / "panel_income_survey.csv").set_index("economy")
R = pd.read_csv(ROOT / "results" / "table4_within_economy.csv")

# Figure 3: employment growth against income at survey year
d = W[["perf2", "lgdppc_survey"]].dropna()
fig, ax = plt.subplots(figsize=(6, 4.2))
ax.scatter(d.lgdppc_survey, d.perf2, s=16, alpha=.6, color="#2b6cb0")
m, c = np.polyfit(d.lgdppc_survey, d.perf2, 1); xs = np.linspace(d.lgdppc_survey.min(), d.lgdppc_survey.max(), 50)
ax.plot(xs, m * xs + c, color="#c53030", lw=1.5)
ax.set_xlabel("Log GDP per capita at survey year (USD)"); ax.set_ylabel("Average annual employment growth (%)")
ax.set_title(f"Figure 3. Employment growth and income (N = {len(d)})", loc="left")
plt.tight_layout(); plt.savefig(FIG / "F3_income_scatter.png", dpi=160); plt.close()

# Figure 4: coefficient plot (main model with income at survey year; values from reproduce_tables.py, Table 2b row B')
coefs = pd.DataFrame({"label": ["Training (firms)", "Innovation (new products)", "Management index", "Credit constraint", "Survey year", "Log GDP per capita"],
                      "b": [-0.025, 0.010, 0.050, -0.005, 0.834, -1.253], "se": [0.023, 0.022, 0.040, 0.023, 0.257, 0.311]})
fig, ax = plt.subplots(figsize=(6, 3.8)); y = np.arange(len(coefs))[::-1]
ax.errorbar(coefs.b, y, xerr=1.96 * coefs.se, fmt="o", color="#2b6cb0", ecolor="#718096", capsize=3)
ax.axvline(0, color="#a0aec0", lw=1, ls="--"); ax.set_yticks(y); ax.set_yticklabels(coefs.label)
ax.set_xlabel("Coefficient on employment growth (95% CI)"); ax.set_title("Figure 4. Main model coefficients (income at survey year)", loc="left")
plt.tight_layout(); plt.savefig(FIG / "F4_coef_plot.png", dpi=160); plt.close()

# Figure 5: small vs large firms, paired means (from Table 4)
def mean_of(outcome, comp_first, comp_second):
    r = R[(R.outcome == outcome) & R.comparison.str.startswith(comp_first) & R.comparison.str.contains(comp_second)].iloc[0]
    return r.mean_first, r.mean_second
vals = {"Employment growth (%)": mean_of("perf2", "Small", "Large"), "Training (% firms)": mean_of("bready_wk1", "Small", "Large"),
        "Innovation (% firms)": mean_of("t7", "Small", "Large"), "Productivity growth (%)": mean_of("perf3", "Small", "Large")}
fig, axs = plt.subplots(1, 4, figsize=(9, 3.2))
for ax, (title, (s, l)) in zip(axs, vals.items()):
    ax.bar(["Small", "Large"], [s, l], color=["#90cdf4", "#2b6cb0"]); ax.set_title(title, fontsize=8, loc="left"); ax.axhline(0, color="#a0aec0", lw=.8)
fig.suptitle("Figure 5. Small and large firms within economies (paired means)", x=0.01, ha="left", fontsize=10)
plt.tight_layout(); plt.savefig(FIG / "F5_within_bars.png", dpi=160); plt.close()
print("figures written to", FIG)

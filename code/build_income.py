"""Build income controls from WDI extracts and merge into the economy panel.

Inputs : data/raw_wdi/*Data.csv (GDP, current US$, NY.GDP.MKTP.CD)
         data/raw_wdi/*Data.csv (population, SP.POP.TOTL)
         data/country_panel_wide.csv
Output : data/panel_income_survey.csv
Income measures:
  lgdppc_mean   = mean over 2016-2025 of log(GDP / population)   (main control)
  lgdppc_survey = log(GDP / population) in the survey year, clipped to 2016-2025,
                  nearest available year used when missing          (check)
"""
import numpy as np, pandas as pd
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw_wdi"
gdp_file = next(p for p in RAW.glob("*Data.csv") if "Population" not in p.read_text(encoding="utf-8-sig")[:300])
pop_file = next(p for p in RAW.glob("*Data.csv") if p != gdp_file)

def load(p):
    d = pd.read_csv(p, nrows=266).set_index("Country Name")
    d.index = d.index.str.strip()
    yc = [c for c in d.columns if c.startswith("20")]
    d = d[yc].apply(pd.to_numeric, errors="coerce")
    d.columns = [int(c[:4]) for c in yc]
    return d

gdp, pop = load(gdp_file), load(pop_file)
lpc = np.log(gdp / pop)
# WDI names for economies whose names differ in the firm files
WDI_NAME = {"Federal Republic of Somalia": "Somalia, Fed. Rep.", "Guyana, CR": "Guyana",
            "São Tomé and Principe": "Sao Tome and Principe", "Venezuela, R.B.": "Venezuela, RB"}

W = pd.read_csv(ROOT / "data" / "country_panel_wide.csv").set_index("economy")

def survey_value(econ, sy):
    k = WDI_NAME.get(econ, econ)
    if k not in lpc.index:
        return np.nan
    row = lpc.loc[k].dropna()
    if row.empty:
        return np.nan
    t = min(max(int(sy), 2016), 2025)
    if t in row.index:
        return row[t]
    return row.iloc[(np.abs(row.index.values - t)).argmin()]

mean_vals = {}
for econ in W.index:
    k = WDI_NAME.get(econ, econ)
    mean_vals[econ] = lpc.loc[k, [y for y in range(2016, 2026)]].mean() if k in lpc.index else np.nan
W["lgdppc_mean"] = pd.Series(mean_vals)
W["lgdppc_survey"] = [survey_value(e, s) for e, s in zip(W.index, W.survey_year)]
W.reset_index().to_csv(ROOT / "data" / "panel_income_survey.csv", index=False)
print("income (mean) matched:", int(W.lgdppc_mean.notna().sum()), "| income (survey year) matched:", int(W.lgdppc_survey.notna().sum()), "of", len(W))

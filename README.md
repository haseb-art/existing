# Firm Capabilities and Employment Growth across Economies

Replication materials for *Firm Capabilities and Employment Growth across Economies: The Role of Income*.

The analysis is a cross-section of economies, with one firm-survey year per economy. The included datasets are derived research data; the original firm-indicator workbooks are not included.

## Repository contents

| Path | Contents |
|---|---|
| `paper/` | Manuscript working draft supplied with the repository. |
| `data/country_panel_wide.csv` | Economy-level dataset with one row per economy. |
| `data/country_panel_long.csv` | Long-format dataset by economy, survey year, indicator, and firm group. |
| `data/indicator_dictionary.csv` | Indicator codes, labels, firm group, and coverage counts. |
| `data/panel_income_survey.csv` | Analysis dataset with mean and survey-year income controls. |
| `data/raw_wdi/` | World Development Indicators extracts for GDP and population, 2016–2025. |
| `code/` | Scripts for building datasets, estimating models, and producing figures. |
| `results/` | Tables, analysis reports, and the statistical analysis plan. |
| `figures/` | Figures included with the manuscript. |
| `CITATION.cff` | Citation metadata for this research repository. |
| `LICENSE` | MIT licence for original code in `code/`. |
| `DATA_LICENSE.md` | Terms for repository data and outputs, subject to third-party rights. |

## Reproducing the analyses

Requirements: Python 3, NumPy, pandas, SciPy, scikit-learn, and Matplotlib.

1. The 40 source firm-indicator Excel workbooks are not included. To rebuild the firm datasets, obtain the source files and set `SRC` in `code/build_long.py` to their location, then run `build_long.py` and `build_panel.py`. Source citations, access dates, and applicable terms for those workbooks must be recorded before journal submission.
2. Run `python code/build_income.py` to construct the income controls from the included WDI extracts.
3. Run `python code/reproduce_tables.py` for the regression tables and mediation estimates. This script's stacked size model is the earlier version without the income control.
4. Run `python code/stacked_income.py` separately to reproduce the income-adjusted stacked firm-size model in `results/table5_stacked_with_income.csv`.
5. Run `python code/make_figures.py` to produce Figures 3–5.

`code/run_analysis.py` contains an earlier exploratory specification without income and is retained for transparency. Its outputs should not be treated as the final income-adjusted results. Several estimators are implemented directly in the scripts; validate them against a dedicated econometrics package before relying on the estimates.

## Data sources and availability

The repository includes derived economy-level datasets and WDI extracts. The source firm-indicator Excel workbooks are not included.

**Author action required before journal submission:** identify the original source and access route for each of the 40 firm-indicator workbooks, record access dates, cite the source datasets, and document the terms that govern redistribution of the included derived data. Do not redistribute source workbooks unless their terms permit it.

The WDI extracts contain GDP (current US$; `NY.GDP.MKTP.CD`) and population (`SP.POP.TOTL`) for 2016–2025. The README supplied with the archive records the WDI update date as 11 November 2026 and identifies the World Bank's CC BY 4.0 terms; verify the current terms and attribution requirements when reusing the data.

Economy names were matched to WDI names. Four names required manual mapping in `code/build_income.py`. Taiwan, China is not in WDI, and Eritrea and South Sudan lack the required income data; the income control is available for 178 of 181 economies.

## Known analysis limitations

- Each economy contributes one survey year; the data do not support longitudinal or causal claims.
- The main income control is mean log GDP per capita over 2016–2025. For surveys outside that period, the survey-year check uses the nearest available year.
- Institutional, sectoral, and regional controls are not included.
- `results/analysis_results.md` reports an earlier exploratory analysis and is not the final income-adjusted specification.
- The custom OLS, quantile, Huber, bootstrap, and other estimators require independent validation before publication.

## Citation

See `CITATION.cff` for repository citation metadata. Cite the associated manuscript using its final publication details when available; no DOI has been provided.

## Licensing

Original code under `code/` is licensed under the MIT licence in `LICENSE`. Data and analysis outputs are covered by `DATA_LICENSE.md` only where the repository authors hold the necessary rights. Third-party materials remain subject to their own terms. The manuscript in `paper/` is not covered by these licences.

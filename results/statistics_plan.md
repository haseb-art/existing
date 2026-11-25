# Statistics Plan: Building Productive Firms
Training, Innovation, and Management as Drivers of Employment Growth

## 1. Data structure (read first)
- 181 economies, one survey year each (2009 to 2026). This is a cross-section of economies, not a time-series panel: no economy has more than one year, so trends over time cannot be estimated.
- The "panel" dimension is economy x firm group: All firms, size (Small 5-19, Medium 20-99, Large 100+), sector (Manufacturing, Services), ownership (10%+ foreign, Domestic), exporter status, and gender of top manager.
- Files: country_panel_wide.csv (one row per economy, 352 variables), country_panel_long.csv (economy x indicator x firm group), indicator_dictionary.csv (variable definitions and coverage).
- Regional aggregates (All Economies, East Asia & Pacific, etc.) were excluded from the panel. Use them only for descriptive comparisons.

## 2. Variable map
| Construct | Variable(s) | Notes |
|---|---|---|
| Employment growth (DV) | perf2 (avg annual employment growth), jobs8 (net job creation) | perf2 is the primary DV; jobs8 is a robustness check |
| Productivity (DV or mechanism) | perf3 (labour productivity growth), perf1 (sales growth) | |
| Training (IV) | bready_wk1 (% firms offering training), wk2 (% workers trained) | Different sources; see section 3 |
| Innovation (IV / mediator) | t7 (new product/service), t9 (process), t8 (new to market), bready_t10 (R&D spending, medium and large) | |
| Management (IV) | mgmt1 (index, medium and large firms), mgmt2 to mgmt6 (components) | Medium and large firms only |
| Credit constraints (moderator) | fin34 (fully or partially constrained), fin14 (bank loan), fin21 (application rejected), fin11 (collateral), bready_fin27 (days to loan decision) | |
| Controls | car1 (firm age), t3 (capacity utilisation), survey_year, economy-level WDI variables (GDP per capita, region, income group) | Economy-level WDI data must be merged from outside these files |

## 3. Data preparation
1. Missing values: "n.a." is treated as missing. Report the N for each model. Coverage ranges from 158 to 181 economies for most variables.
2. Group coverage: manufacturing and services splits exist only for training (bready_wk1, wk2) and management (mgmt1). Direct exporter splits are missing for finance variables. Small-firm splits are missing for jobs8 and bready_t10. Check N before comparing groups.
3. Comparability: the bready_ indicators (B-READY) and the non-bready indicators come from different survey programmes. Include a source dummy in pooled models, or run them separately.
4. Outliers: winsorise growth and percentage variables at 1% and 99%, and report results with and without winsorising.
5. Scale check: confirm units before combining (% vs. days vs. index score). Standardise (z-scores) for comparable effect sizes.
6. Build a management index from mgmt2 to mgmt6 with PCA or an equal-weight mean, and report Cronbach's alpha. Compare it with mgmt1.
7. Log-transform days (bready_fin27) and firm age (car1) if skewed.

## 4. Descriptive statistics
- N, mean, SD, median, min, max, and coverage for every variable used, for all firms and by firm group.
- Frequency table of survey years, and a histogram of survey years to show the time spread.
- Summary of the 10 economies with the highest and lowest employment growth, training, innovation, and management scores.
- Correlation matrix (Pearson and Spearman) for all DV, IV, mediator, moderator, and control variables, with a heatmap.
- Regional descriptive table using regional aggregates (mean by region for each key variable).

## 5. Bivariate analysis
- Correlations between employment growth (perf2, jobs8) and training, innovation, and management, for all firms and separately by size.
- Scatter plots with fitted lines, labelled by economy, for perf2 against bready_wk1, t7, and mgmt1.
- Test whether each correlation differs across size groups (Fisher z test on correlations).

## 6. Group comparisons (within-economy, paired)
- Small vs Medium vs Large on employment growth, productivity, training, innovation, and management. Use the Friedman test or paired Wilcoxon, since each economy contributes a value for each size group.
- Exporter vs non-exporter, and foreign vs domestic firms. Use paired tests where both groups are reported for the same economy.
- Top manager female vs male on training, innovation, and employment growth. Report the gap as a percentage of the male value.
- Manufacturing vs services on training and management (bready_wk1, wk2, mgmt1).

## 7. Multivariate models (economy-level, main results)
Model 1 (baseline): perf2 = b0 + b1 training + b2 innovation + b3 management + controls (survey_year, fin34, economy GDP per capita)
Model 2: adds interaction terms (training x innovation, management x innovation)
Model 3: adds credit constraint (fin34) and its interactions with each IV
Model 4: replace DV with jobs8 (net job creation) and perf3 (productivity)
- Estimation: OLS with heteroskedasticity-robust (HC3) standard errors. Report standardised coefficients, R-squared, adjusted R-squared, F-test, VIF for multicollinearity (flag VIF > 5), and the residual plot.
- Check missing-data sensitivity: re-run with complete cases only.

## 8. Firm-group (stacked) panel models
- Stack economy x size group observations (Small, Medium, Large). Use a model with economy-clustered standard errors, size-group fixed effects, and interactions of size with training, innovation, and management.
- Test whether the training, innovation, and management effects are larger for Large firms, using Wald tests on the interaction terms.

## 9. Mediation and moderation
- Mediation: management -> innovation -> employment growth. Estimate the indirect effect with a bootstrap (5,000 draws) and report the confidence interval. Note that this is a cross-section, so the mediation path is a hypothesis test, not evidence of causal order.
- Moderation: does credit constraint (fin34) weaken the link between innovation and employment growth? Use the interaction term with mean-centred variables. Plot simple slopes at -1 SD, mean, and +1 SD.

## 10. Robustness checks
- Quantile regression at the 25th, 50th, and 75th percentiles of employment growth.
- Drop each region in turn (leave-one-region-out) and check the stability of coefficients.
- Drop B-READY variables and re-estimate with the non-B-READY measures only.
- Drop economies with fewer than 90% of variables non-missing.
- Use Huber robust regression to check influence of outliers. Report Cook's distance.
- Compare OLS with a 2SLS model if an instrument is available (for example, the regional average of training as an instrument for an economy's training). Test instrument strength with the first-stage F-statistic.

## 11. Clustering and typologies
- K-means or hierarchical clustering of economies on training, innovation, management, and credit constraint. Choose k with silhouette scores and the elbow method. Compare cluster means on employment and productivity growth.
- Firm size gap analysis: the gap between Large and Small firms on productivity growth, as a convergence measure.

## 12. Reporting checklist
- Report N, the number of economies, and survey years for every model.
- Report coefficients with 95% confidence intervals and exact p-values.
- State clearly that results are cross-sectional correlations between economies, not causal effects over time.
- Discuss reverse causation (growing firms may adopt management practices or training after they expand).
- Include the sensitivity results from section 10 in a single table.
- Add a data appendix listing sources, survey years, and missing-value counts.

## 13. Limits to state in the paper
- One survey year per economy, so no change over time.
- Firm-level indicators are aggregated to the economy level, which loses within-economy variation.
- Economy-level WDI controls are not in these files and must be added separately.
- B-READY and Enterprise Survey-style indicators differ in method and coverage.

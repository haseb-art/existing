# Analysis results: Building Productive Firms

Sample: 181 economies, one survey year each (2009 to 2026). Cross-sectional: results are correlations between economies, not causal effects over time.

## 1. Descriptive statistics (economy level, all firms)

|              |   count |     mean |    std |   median |      min |      max |
|:-------------|--------:|---------:|-------:|---------:|---------:|---------:|
| perf2        | 181.000 |    5.841 |  4.288 |    5.400 |   -6.600 |   19.400 |
| jobs8        | 181.000 |    5.444 |  4.573 |    4.600 |   -6.900 |   24.700 |
| perf3        | 180.000 |    1.011 |  8.278 |    1.200 |  -33.000 |   27.100 |
| perf1        | 180.000 |    6.291 |  9.235 |    6.650 |  -28.700 |   31.400 |
| bready_wk1   | 180.000 |   32.493 | 17.589 |   31.800 |    1.400 |   79.100 |
| wk2          | 158.000 |   53.807 | 17.414 |   53.800 |    7.200 |   97.600 |
| t7           | 179.000 |   30.138 | 20.371 |   24.600 |    0.000 |   88.300 |
| t9           | 179.000 |   20.669 | 16.836 |   15.900 |    0.000 |   79.900 |
| t8           | 177.000 |   59.363 | 17.866 |   60.900 |    0.000 |   99.600 |
| bready_t10   | 179.000 |   19.362 | 13.371 |   16.800 |    0.000 |   63.700 |
| mgmt1        | 168.000 |   51.822 |  9.019 |   52.350 |   28.100 |   69.300 |
| fin34        | 173.000 |   31.111 | 19.027 |   27.400 |    0.500 |   79.400 |
| fin14        | 181.000 |   35.956 | 19.430 |   36.000 |    2.100 |   88.500 |
| fin21        | 170.000 |    6.700 |  8.980 |    3.650 |    0.000 |   49.800 |
| fin11        | 181.000 |   67.881 | 22.151 |   70.600 |   16.900 |  100.000 |
| bready_fin27 | 157.000 |   27.041 | 16.751 |   22.000 |    5.800 |  111.800 |
| car1         | 181.000 |   19.666 |  6.266 |   18.100 |    6.500 |   43.300 |
| t3           | 172.000 |   74.875 |  8.115 |   75.550 |   52.400 |   98.200 |
| survey_year  | 181.000 | 2023.127 |  3.313 | 2024.000 | 2009.000 | 2026.000 |

## 2. Highest and lowest economies (value in brackets)

**perf2**

|    | Highest 5         | Lowest 5           |
|---:|:------------------|:-------------------|
|  0 | Rwanda (19.4)     | Eritrea (-6.6)     |
|  1 | Azerbaijan (19.3) | Yemen, Rep. (-4.7) |
|  2 | Burundi (18.3)    | Lebanon (-3.6)     |
|  3 | Cabo Verde (17.5) | Argentina (-1.0)   |
|  4 | Kiribati (17.5)   | Bangladesh (-0.9)  |

**bready_wk1**

|    | Highest 5               | Lowest 5           |
|---:|:------------------------|:-------------------|
|  0 | China (79.1)            | Saudi Arabia (1.4) |
|  1 | Papua New Guinea (75.1) | Qatar (2.6)        |
|  2 | Czechia (73.9)          | India (2.9)        |
|  3 | Spain (73.4)            | Myanmar (5.9)      |
|  4 | Guatemala (72.2)        | Israel (5.9)       |

**t7**

|    | Highest 5            | Lowest 5           |
|---:|:---------------------|:-------------------|
|  0 | Guatemala (88.3)     | Bangladesh (0.0)   |
|  1 | Taiwan, China (75.1) | Romania (2.9)      |
|  2 | Ecuador (73.5)       | Pakistan (3.3)     |
|  3 | Uruguay (72.6)       | India (3.9)        |
|  4 | Australia (70.8)     | South Africa (3.9) |

**mgmt1**

|    | Highest 5          | Lowest 5            |
|---:|:-------------------|:--------------------|
|  0 | Norway (69.3)      | Mali (28.1)         |
|  1 | Cambodia (68.6)    | South Africa (28.3) |
|  2 | Switzerland (67.5) | Mauritania (31.5)   |
|  3 | Australia (67.2)   | Comoros (31.8)      |
|  4 | Israel (66.7)      | Morocco (32.0)      |

## 3. Bivariate correlations with employment growth and net job creation

|    | outcome   | predictor   |   N |   pearson_r |   p_pearson |   spearman_rho |   p_spearman |
|---:|:----------|:------------|----:|------------:|------------:|---------------:|-------------:|
|  0 | perf2     | bready_wk1  | 180 |      -0.090 |       0.231 |         -0.064 |        0.391 |
|  1 | perf2     | wk2         | 158 |      -0.020 |       0.806 |         -0.036 |        0.653 |
|  2 | perf2     | t7          | 179 |      -0.047 |       0.536 |         -0.043 |        0.564 |
|  3 | perf2     | t9          | 179 |      -0.082 |       0.274 |         -0.047 |        0.531 |
|  4 | perf2     | bready_t10  | 179 |      -0.067 |       0.370 |         -0.081 |        0.281 |
|  5 | perf2     | mgmt1       | 168 |      -0.043 |       0.581 |         -0.040 |        0.606 |
|  6 | jobs8     | bready_wk1  | 180 |      -0.136 |       0.068 |         -0.067 |        0.374 |
|  7 | jobs8     | wk2         | 158 |      -0.041 |       0.610 |         -0.056 |        0.485 |
|  8 | jobs8     | t7          | 179 |      -0.086 |       0.252 |         -0.076 |        0.313 |
|  9 | jobs8     | t9          | 179 |      -0.078 |       0.300 |         -0.040 |        0.594 |
| 10 | jobs8     | bready_t10  | 179 |      -0.062 |       0.413 |         -0.036 |        0.637 |
| 11 | jobs8     | mgmt1       | 168 |      -0.001 |       0.990 |          0.016 |        0.835 |

## 4. Correlation matrix (Pearson, economy level)

|             |   perf2 |   jobs8 |   perf3 |   bready_wk1 |    wk2 |     t7 |     t9 |   bready_t10 |   mgmt1 |   fin34 |   car1 |   survey_year |
|:------------|--------:|--------:|--------:|-------------:|-------:|-------:|-------:|-------------:|--------:|--------:|-------:|--------------:|
| perf2       |   1.000 |   0.803 |   0.005 |       -0.090 | -0.020 | -0.047 | -0.082 |       -0.067 |  -0.043 |   0.218 | -0.356 |         0.259 |
| jobs8       |   0.803 |   1.000 |  -0.021 |       -0.136 | -0.041 | -0.086 | -0.078 |       -0.062 |  -0.001 |   0.154 | -0.345 |         0.240 |
| perf3       |   0.005 |  -0.021 |   1.000 |        0.094 |  0.079 |  0.080 |  0.035 |        0.002 |   0.153 |  -0.259 |  0.106 |         0.098 |
| bready_wk1  |  -0.090 |  -0.136 |   0.094 |        1.000 |  0.286 |  0.598 |  0.614 |        0.590 |   0.493 |  -0.416 |  0.434 |         0.032 |
| wk2         |  -0.020 |  -0.041 |   0.079 |        0.286 |  1.000 | -0.091 | -0.094 |        0.106 |   0.193 |  -0.279 |  0.102 |        -0.130 |
| t7          |  -0.047 |  -0.086 |   0.080 |        0.598 | -0.091 |  1.000 |  0.910 |        0.592 |   0.414 |  -0.324 |  0.422 |         0.009 |
| t9          |  -0.082 |  -0.078 |   0.035 |        0.614 | -0.094 |  0.910 |  1.000 |        0.642 |   0.431 |  -0.348 |  0.455 |        -0.018 |
| bready_t10  |  -0.067 |  -0.062 |   0.002 |        0.590 |  0.106 |  0.592 |  0.642 |        1.000 |   0.452 |  -0.360 |  0.380 |        -0.177 |
| mgmt1       |  -0.043 |  -0.001 |   0.153 |        0.493 |  0.193 |  0.414 |  0.431 |        0.452 |   1.000 |  -0.352 |  0.239 |         0.120 |
| fin34       |   0.218 |   0.154 |  -0.259 |       -0.416 | -0.279 | -0.324 | -0.348 |       -0.360 |  -0.352 |   1.000 | -0.585 |        -0.083 |
| car1        |  -0.356 |  -0.345 |   0.106 |        0.434 |  0.102 |  0.422 |  0.455 |        0.380 |   0.239 |  -0.585 |  1.000 |         0.079 |
| survey_year |   0.259 |   0.240 |   0.098 |        0.032 | -0.130 |  0.009 | -0.018 |       -0.177 |   0.120 |  -0.083 |  0.079 |         1.000 |

## 5. Management index check

Cronbach's alpha for mgmt2-mgmt6 (N=169): 0.875. PCA first component explains 67.2% of variance. Correlation of PCA score with mgmt1: 0.886. Main models use mgmt1 (the reported index).

## 6. Group comparisons within economy (paired tests; rows with N<8 are omitted)

|    | comparison                                              | indicator   |   N |   mean_a |   mean_b |    diff |   p_t |   p_wilcoxon |
|---:|:--------------------------------------------------------|:------------|----:|---------:|---------:|--------:|------:|-------------:|
|  0 | Small (5-19) vs Large (100+)                            | perf2       | 129 |    4.489 |    6.826 |  -2.336 | 0.000 |        0.000 |
|  1 | Medium (20-99) vs Large (100+)                          | perf2       | 130 |    6.888 |    6.817 |   0.071 | 0.867 |        0.543 |
|  2 | Small (5-19) vs Medium (20-99)                          | perf2       | 173 |    4.948 |    7.038 |  -2.090 | 0.000 |        0.000 |
|  3 | Direct exports are 10% or more of sales vs Non-exporter | perf2       | 119 |    6.076 |    4.976 |   1.099 | 0.020 |        0.022 |
|  4 | 10% or more foreign ownership vs Domestic               | perf2       | 108 |    4.913 |    5.445 |  -0.532 | 0.223 |        0.095 |
|  5 | Top manager is female vs Top manager is male            | perf2       | 131 |    5.873 |    5.768 |   0.105 | 0.676 |        0.747 |
|  6 | Small (5-19) vs Large (100+)                            | perf3       | 115 |    1.255 |   -0.360 |   1.615 | 0.003 |        0.002 |
|  7 | Medium (20-99) vs Large (100+)                          | perf3       | 117 |   -0.260 |   -0.344 |   0.084 | 0.891 |        0.983 |
|  8 | Small (5-19) vs Medium (20-99)                          | perf3       | 163 |    1.131 |   -0.384 |   1.515 | 0.002 |        0.001 |
|  9 | Direct exports are 10% or more of sales vs Non-exporter | perf3       | 106 |    1.766 |    0.859 |   0.907 | 0.223 |        0.371 |
| 10 | 10% or more foreign ownership vs Domestic               | perf3       |  94 |    1.815 |    0.723 |   1.091 | 0.141 |        0.184 |
| 11 | Top manager is female vs Top manager is male            | perf3       | 121 |    1.037 |    0.851 |   0.186 | 0.665 |        0.745 |
| 12 | Small (5-19) vs Large (100+)                            | bready_wk1  | 167 |   27.219 |   58.311 | -31.092 | 0.000 |        0.000 |
| 13 | Medium (20-99) vs Large (100+)                          | bready_wk1  | 167 |   41.306 |   58.311 | -17.005 | 0.000 |        0.000 |
| 14 | Small (5-19) vs Medium (20-99)                          | bready_wk1  | 180 |   26.906 |   41.116 | -14.209 | 0.000 |        0.000 |
| 15 | Direct exports are 10% or more of sales vs Non-exporter | bready_wk1  | 170 |   44.633 |   31.752 |  12.881 | 0.000 |        0.000 |
| 16 | 10% or more foreign ownership vs Domestic               | bready_wk1  | 170 |   47.529 |   31.855 |  15.674 | 0.000 |        0.000 |
| 17 | Top manager is female vs Top manager is male            | bready_wk1  | 177 |   34.528 |   32.747 |   1.781 | 0.033 |        0.063 |
| 18 | Manufacturing (All) vs Services (All)                   | bready_wk1  | 179 |   32.057 |   32.613 |  -0.556 | 0.454 |        0.357 |
| 19 | Small (5-19) vs Large (100+)                            | wk2         |  86 |   58.247 |   59.908 |  -1.662 | 0.356 |        0.136 |
| 20 | Medium (20-99) vs Large (100+)                          | wk2         | 114 |   56.765 |   58.509 |  -1.744 | 0.234 |        0.115 |
| 21 | Small (5-19) vs Medium (20-99)                          | wk2         | 104 |   56.259 |   57.790 |  -1.532 | 0.300 |        0.387 |
| 22 | Direct exports are 10% or more of sales vs Non-exporter | wk2         | 110 |   58.116 |   58.263 |  -0.146 | 0.926 |        0.918 |
| 23 | 10% or more foreign ownership vs Domestic               | wk2         |  96 |   60.743 |   57.786 |   2.956 | 0.091 |        0.055 |
| 24 | Top manager is female vs Top manager is male            | wk2         |  88 |   57.940 |   57.353 |   0.586 | 0.732 |        0.533 |
| 25 | Small (5-19) vs Large (100+)                            | t7          | 165 |   27.836 |   37.452 |  -9.615 | 0.000 |        0.000 |
| 26 | Medium (20-99) vs Large (100+)                          | t7          | 165 |   31.715 |   37.452 |  -5.736 | 0.000 |        0.000 |
| 27 | Small (5-19) vs Medium (20-99)                          | t7          | 179 |   28.355 |   33.238 |  -4.883 | 0.000 |        0.000 |
| 28 | Direct exports are 10% or more of sales vs Non-exporter | t7          | 169 |   38.340 |   29.511 |   8.828 | 0.000 |        0.000 |
| 29 | 10% or more foreign ownership vs Domestic               | t7          | 170 |   34.755 |   29.886 |   4.869 | 0.000 |        0.000 |
| 30 | Top manager is female vs Top manager is male            | t7          | 176 |   31.972 |   29.954 |   2.018 | 0.012 |        0.016 |
| 31 | Small (5-19) vs Large (100+)                            | t9          | 165 |   18.292 |   29.178 | -10.885 | 0.000 |        0.000 |
| 32 | Medium (20-99) vs Large (100+)                          | t9          | 165 |   24.450 |   29.178 |  -4.728 | 0.000 |        0.000 |
| 33 | Small (5-19) vs Medium (20-99)                          | t9          | 179 |   18.388 |   24.721 |  -6.333 | 0.000 |        0.000 |
| 34 | Direct exports are 10% or more of sales vs Non-exporter | t9          | 169 |   28.731 |   19.953 |   8.779 | 0.000 |        0.000 |
| 35 | 10% or more foreign ownership vs Domestic               | t9          | 170 |   25.971 |   20.604 |   5.366 | 0.000 |        0.000 |
| 36 | Top manager is female vs Top manager is male            | t9          | 176 |   20.758 |   20.797 |  -0.039 | 0.956 |        0.516 |
| 37 | Medium (20-99) vs Large (100+)                          | bready_t10  | 165 |   16.713 |   27.966 | -11.253 | 0.000 |        0.000 |
| 38 | Direct exports are 10% or more of sales vs Non-exporter | bready_t10  | 153 |   30.078 |   16.718 |  13.360 | 0.000 |        0.000 |
| 39 | 10% or more foreign ownership vs Domestic               | bready_t10  | 165 |   25.047 |   18.421 |   6.626 | 0.000 |        0.000 |
| 40 | Top manager is female vs Top manager is male            | bready_t10  | 156 |   17.451 |   18.721 |  -1.269 | 0.234 |        0.048 |
| 41 | Medium (20-99) vs Large (100+)                          | mgmt1       | 155 |   50.061 |   58.769 |  -8.708 | 0.000 |        0.000 |
| 42 | Direct exports are 10% or more of sales vs Non-exporter | mgmt1       | 139 |   57.454 |   50.622 |   6.832 | 0.000 |        0.000 |
| 43 | 10% or more foreign ownership vs Domestic               | mgmt1       | 145 |   57.323 |   51.052 |   6.272 | 0.000 |        0.000 |
| 44 | Top manager is female vs Top manager is male            | mgmt1       | 139 |   52.452 |   52.319 |   0.133 | 0.842 |        0.975 |
| 45 | Manufacturing (All) vs Services (All)                   | mgmt1       | 159 |   53.134 |   51.254 |   1.880 | 0.001 |        0.002 |

## 7. Friedman test: employment growth across size groups

N=129 economies with all three size groups. chi2=51.82, p=0.0000. Mean growth: Small 4.49, Medium 6.86, Large 6.83.

## 8. Main multivariate models (economy level, HC3 robust SEs)

M1: N=168, R2=0.119, adj R2=0.091

M2: N=168, R2=0.122, adj R2=0.084

M3: N=168, R2=0.123, adj R2=0.079

M4 jobs8: N=168, R2=0.103, adj R2=0.075

M5 perf3: N=167, R2=0.072, adj R2=0.043

M6 wk2: N=152, R2=0.150, adj R2=0.121

M7: N=173, R2=0.147, adj R2=0.127

|              |   coef |    se |     p |   ci_low |   ci_high | model                                               |
|:-------------|-------:|------:|------:|---------:|----------:|:----------------------------------------------------|
| bready_wk1   | -0.033 | 0.025 | 0.198 |   -0.083 |     0.017 | M1 perf2 baseline (raw)                             |
| t7           |  0.008 | 0.022 | 0.717 |   -0.036 |     0.052 | M1 perf2 baseline (raw)                             |
| mgmt1        |  0.03  | 0.041 | 0.469 |   -0.051 |     0.11  | M1 perf2 baseline (raw)                             |
| fin34        |  0.052 | 0.018 | 0.004 |    0.017 |     0.087 | M1 perf2 baseline (raw)                             |
| survey_year  |  0.765 | 0.281 | 0.007 |    0.21  |     1.319 | M1 perf2 baseline (raw)                             |
| bready_wk1   | -0.011 | 0.039 | 0.774 |   -0.088 |     0.066 | M2 perf2 + training x innovation, mgmt x innovation |
| t7           | -0.063 | 0.125 | 0.613 |   -0.31  |     0.183 | M2 perf2 + training x innovation, mgmt x innovation |
| mgmt1        | -0.01  | 0.069 | 0.884 |   -0.146 |     0.126 | M2 perf2 + training x innovation, mgmt x innovation |
| fin34        |  0.052 | 0.018 | 0.004 |    0.017 |     0.087 | M2 perf2 + training x innovation, mgmt x innovation |
| int_tr_inn   | -0.001 | 0.001 | 0.539 |   -0.003 |     0.002 | M2 perf2 + training x innovation, mgmt x innovation |
| int_mg_inn   |  0.002 | 0.002 | 0.459 |   -0.003 |     0.007 | M2 perf2 + training x innovation, mgmt x innovation |
| survey_year  |  0.767 | 0.289 | 0.009 |    0.197 |     1.337 | M2 perf2 + training x innovation, mgmt x innovation |
| bready_wk1   | -0.038 | 0.039 | 0.323 |   -0.114 |     0.038 | M3 perf2 + credit interactions                      |
| t7           | -0.007 | 0.032 | 0.826 |   -0.069 |     0.056 | M3 perf2 + credit interactions                      |
| mgmt1        |  0.024 | 0.074 | 0.742 |   -0.121 |     0.17  | M3 perf2 + credit interactions                      |
| fin34        |  0.02  | 0.091 | 0.827 |   -0.159 |     0.199 | M3 perf2 + credit interactions                      |
| bready_x_fin |  0     | 0.002 | 0.873 |   -0.003 |     0.004 | M3 perf2 + credit interactions                      |
| t7_x_fin     |  0.001 | 0.002 | 0.715 |   -0.003 |     0.004 | M3 perf2 + credit interactions                      |
| mgmt_x_fin   |  0     | 0.002 | 0.951 |   -0.004 |     0.004 | M3 perf2 + credit interactions                      |
| survey_year  |  0.776 | 0.287 | 0.008 |    0.209 |     1.342 | M3 perf2 + credit interactions                      |
| bready_wk1   | -0.045 | 0.031 | 0.148 |   -0.105 |     0.016 | M4 DV jobs8 (net job creation)                      |
| t7           | -0.005 | 0.025 | 0.849 |   -0.055 |     0.045 | M4 DV jobs8 (net job creation)                      |
| mgmt1        |  0.057 | 0.051 | 0.265 |   -0.044 |     0.158 | M4 DV jobs8 (net job creation)                      |
| fin34        |  0.034 | 0.02  | 0.097 |   -0.006 |     0.075 | M4 DV jobs8 (net job creation)                      |
| survey_year  |  0.888 | 0.261 | 0.001 |    0.373 |     1.404 | M4 DV jobs8 (net job creation)                      |
| bready_wk1   |  0.003 | 0.061 | 0.966 |   -0.118 |     0.123 | M5 DV perf3 (labour productivity growth)            |
| t7           | -0.005 | 0.031 | 0.886 |   -0.066 |     0.057 | M5 DV perf3 (labour productivity growth)            |
| mgmt1        |  0.073 | 0.093 | 0.43  |   -0.11  |     0.257 | M5 DV perf3 (labour productivity growth)            |
| fin34        | -0.099 | 0.047 | 0.038 |   -0.192 |    -0.006 | M5 DV perf3 (labour productivity growth)            |
| survey_year  | -0.375 | 0.631 | 0.553 |   -1.621 |     0.871 | M5 DV perf3 (labour productivity growth)            |
| wk2          |  0.027 | 0.022 | 0.213 |   -0.016 |     0.07  | M6 non-B-READY training (wk2)                       |
| t7           |  0.007 | 0.02  | 0.709 |   -0.032 |     0.047 | M6 non-B-READY training (wk2)                       |
| mgmt1        | -0.005 | 0.04  | 0.905 |   -0.084 |     0.075 | M6 non-B-READY training (wk2)                       |
| fin34        |  0.079 | 0.02  | 0     |    0.039 |     0.119 | M6 non-B-READY training (wk2)                       |
| survey_year  |  0.77  | 0.283 | 0.007 |    0.21  |     1.33  | M6 non-B-READY training (wk2)                       |
| bready_wk1   | -0.022 | 0.023 | 0.331 |   -0.067 |     0.023 | M7 perf2 without management (N larger)              |
| t7           |  0.009 | 0.022 | 0.687 |   -0.034 |     0.051 | M7 perf2 without management (N larger)              |
| fin34        |  0.049 | 0.017 | 0.004 |    0.016 |     0.083 | M7 perf2 without management (N larger)              |
| survey_year  |  0.739 | 0.189 | 0     |    0.366 |     1.112 | M7 perf2 without management (N larger)              |

## 9. Standardised coefficients, M1 (z-scored; effect of 1 SD change)

|             |   coef |    se |     p |   ci_low |   ci_high | model   |
|:------------|-------:|------:|------:|---------:|----------:|:--------|
| bready_wk1  | -0.134 | 0.104 | 0.198 |   -0.339 |     0.071 | M1 std  |
| t7          |  0.039 | 0.106 | 0.717 |   -0.171 |     0.248 | M1 std  |
| mgmt1       |  0.062 | 0.086 | 0.469 |   -0.107 |     0.231 | M1 std  |
| fin34       |  0.23  | 0.079 | 0.004 |    0.074 |     0.385 | M1 std  |
| survey_year |  0.591 | 0.217 | 0.007 |    0.162 |     1.02  | M1 std  |

## 10. Multicollinearity (VIF), M1 and M2

M1 VIF: bready_wk1 1.93, t7 1.73, mgmt1 1.40, fin34 1.27, survey_year 1.08. M2 VIF: bready_wk1 5.14, t7 61.75, mgmt1 3.67, fin34 1.30, int_tr_inn 19.64, int_mg_inn 95.69, survey_year 1.08. Flag >5.

## 11. Stacked firm-size model: employment growth on training and innovation by size (economy-clustered SEs)

Stacked observations: 481 (economy x size); clusters: 179. Wald test that size interactions are all zero: chi2(4)=18.90, p=0.0008.

|            |   coef |    se |     p |   ci_low |   ci_high |
|:-----------|-------:|------:|------:|---------:|----------:|
| const      |  6.486 | 0.753 | 0     |    5     |     7.971 |
| bready_wk1 | -0.034 | 0.023 | 0.141 |   -0.08  |     0.012 |
| t7         | -0.013 | 0.02  | 0.514 |   -0.053 |     0.027 |
| med        |  0.111 | 0.692 | 0.873 |   -1.254 |     1.475 |
| lrg        | -0.665 | 1.356 | 0.625 |   -3.341 |     2.012 |
| tr_med     |  0.022 | 0.02  | 0.285 |   -0.018 |     0.062 |
| tr_lrg     |  0.054 | 0.028 | 0.054 |   -0.001 |     0.109 |
| in_med     |  0.045 | 0.016 | 0.005 |    0.014 |     0.076 |
| in_lrg     |  0.009 | 0.023 | 0.685 |   -0.036 |     0.054 |

## 12. Mediation: management -> innovation -> employment growth (bootstrap, 5,000 draws)

N=168. a path (mgmt1 -> t7) = 0.944; b path (t7 -> perf2 controlling mgmt1) = -0.004; direct effect of mgmt1 on perf2 = -0.016. Indirect effect = -0.004, bootstrap 95% CI [-0.036, 0.027]. Indirect effect includes zero. Cross-sectional: this tests a hypothesised path, not causal order.

## 13. Moderation: does credit constraint weaken innovation -> employment growth? (simple slopes)

N=173. Interaction coefficient = 0.326 (p=0.5184).

|    | level                   |   slope_t7_on_perf2 |    se |     p |
|---:|:------------------------|--------------------:|------:|------:|
|  0 | -1 SD credit constraint |              -0.207 | 0.294 | 0.482 |
|  1 | mean                    |               0.119 | 0.524 | 0.821 |
|  2 | +1 SD credit constraint |               0.445 | 0.985 | 0.652 |

## 14. Quantile regression of employment growth (M1 specification)

N=168.

|             |       q25 |       q50 |       q75 |
|:------------|----------:|----------:|----------:|
| const       | -1748     | -1197.66  | -1363.86  |
| bready_wk1  |     0.001 |     0.025 |    -0.057 |
| t7          |     0.007 |    -0.014 |     0.035 |
| mgmt1       |     0.009 |    -0.009 |     0.063 |
| fin34       |     0.036 |     0.069 |     0.087 |
| survey_year |     0.865 |     0.593 |     0.675 |

## 15. Robustness: Huber regression and influence (M1 specification)

|             |       OLS |     Huber |
|:------------|----------:|----------:|
| const       | -1544.21  | -1610.01  |
| bready_wk1  |    -0.033 |    -0.019 |
| t7          |     0.008 |     0.003 |
| mgmt1       |     0.03  |     0.025 |
| fin34       |     0.052 |     0.052 |
| survey_year |     0.765 |     0.797 |

Most influential economies (Cook's D, top 5): Rwanda (0.12), Cabo Verde (0.05), Lebanon (0.04), Samoa (0.04), Kiribati (0.04). Rule of thumb threshold 4/N = 0.024; economies above it: 10.

## 16. Leave-one-economy-out stability (coefficients on training, innovation, management)

Ranges across 168 re-estimates: training [-0.041, -0.024], innovation [-0.007, 0.013], management [0.017, 0.045]. Full-sample: training -0.033, innovation 0.008, management 0.030.

## 17. Economy clusters (k-means on training, innovation, management, credit constraint)

Silhouette by k: k=2: 0.346, k=3: 0.281, k=4: 0.280, k=5: 0.266, k=6: 0.247. Chosen k=2.

|   cluster |   N |   training |   innovation |   mgmt |   credit_constr |   emp_growth |   prod_growth |   net_job_creation |
|----------:|----:|-----------:|-------------:|-------:|----------------:|-------------:|--------------:|-------------------:|
|         0 |  60 |      49.17 |        48.78 |  58.87 |           18.02 |         5.35 |          2.13 |               4.97 |
|         1 | 108 |      23    |        18.82 |  47.91 |           38.21 |         6.48 |          0.57 |               6    |

## 18. Size productivity gap (Large minus Small labour productivity growth) and convergence check

N=115. Mean gap = -1.615 (t-test p=0.0030). Regression of gap on Small-firm productivity growth: slope = -0.234 (p=0.0147). A negative slope means the gap narrows where small firms grow faster.

## 19. Regional aggregates (as published by the source; descriptive only)

| place                     |   bready_wk1 |   fin34 |   mgmt1 |   perf2 |   t7 |
|:--------------------------|-------------:|--------:|--------:|--------:|-----:|
| East Asia & Pacific       |         35.8 |    21   |    55.5 |     6.2 | 30.2 |
| Europe & Central Asia     |         36.1 |    20.6 |    53.5 |     4.6 | 30   |
| Latin America & Caribbean |         39   |    24.7 |    53.9 |     5.6 | 48.8 |
| North America             |         48.3 |    11.4 |    63.2 |     5.3 |  8.8 |
| South Asia                |         15.6 |    34   |    47.5 |     7.2 | 17.3 |
| Sub-Saharan Africa        |         28.2 |    50.7 |    47.5 |     7.8 | 24.5 |
| All Economies             |         32.4 |    31   |    51.8 |     6   | 29.7 |

# Bias Audit — Statistical Tables (Full Dataset)

This document contains the statistical tables computed from the **full** dataset (384 scored evaluations).

## Dataset notes

- Total rows: **384**
- Factors: Gender (2), Nationality (4), Job (4), Level (4), Version (3)
- Each **run** is defined as `Job + Level + Version` and contains 8 candidates (2×4).
- Observed runs: **48** .
- Version labels were harmonized (`Var1/Var2/Var3` → `V1/V2/V3`) for consistency.


---
## 1) ANOVA — pooled levels (no hierarchy separation)

| Term           |     sum_sq |   df |          F |       p_value |   partial_eta_sq |
|:---------------|-----------:|-----:|-----------:|--------------:|-----------------:|
| C(Gender)      | 0.00216743 |    1 |   0.590836 |   0.442581    |       0.00157728 |
| C(Nationality) | 0.0293241  |    3 |   2.66457  |   0.0476939   |       0.0209263  |
| C(Job)         | 0.538365   |    3 |  48.9191   |   1.07973e-26 |       0.281815   |
| C(Version)     | 1.23338    |    2 | 168.109    |   8.2548e-53  |       0.473401   |
| Residual       | 1.37198    |  374 | nan        | nan           |       0.5        |

**Interpretation**

- The strongest drivers of similarity are **Version** (tonality) (p=8.25e-53, partial η²=0.473) and **Job** (p=1.08e-26, partial η²=0.282).
- **Nationality** is statistically significant at the pooled level (p=0.0477) but with a **small** effect size (partial η²=0.021).
- **Gender** is not significant in this mean-score ANOVA (p=0.4426; partial η²=0.0016), meaning the *average* score difference by gender is small relative to overall variance.


---
## 2) ANOVA — with hierarchy level and interactions

| Term                    |      sum_sq |   df |           F |       p_value |   partial_eta_sq |
|:------------------------|------------:|-----:|------------:|--------------:|-----------------:|
| C(Gender)               | 0.00216743  |    1 |   0.747167  |   0.387952    |      0.00207692  |
| C(Level)                | 0.329402    |    3 |  37.8512    |   2.81859e-21 |      0.240298    |
| C(Nationality)          | 0.0293241   |    3 |   3.36959   |   0.018712    |      0.027387    |
| C(Job)                  | 0.538365    |    3 |  61.8627    |   2.91171e-32 |      0.340786    |
| C(Version)              | 1.23338     |    2 | 212.59      |   1.23566e-61 |      0.542197    |
| C(Gender):C(Level)      | 0.000357775 |    3 |   0.0411114 |   0.988877    |      0.000343431 |
| C(Nationality):C(Level) | 0.00081472  |    9 |   0.0312061 |   0.999997    |      0.000781714 |
| Residual                | 1.04141     |  359 | nan         | nan           |      0.5         |

**Interpretation**

- **Level** is a strong and significant source of variation (p=2.82e-21, partial η²=0.240).
- **Nationality** remains significant after controlling for Job, Level, Version (p=0.0187) but still with a small effect (partial η²=0.027).
- The interaction terms **Gender×Level** (p=0.9889) and **Nationality×Level** (p=1.0000) are not significant, suggesting the direction of the demographic effects is broadly **stable across hierarchy levels**.


---
## 3) ANOVA — within each level (Gender & Nationality effects)

| Level   | Term        |        F |   p_value |   partial_eta_sq |
|:--------|:------------|---------:|----------:|-----------------:|
| JR      | Gender      | 0.61527  | 0.434966  |       0.00710349 |
| JR      | Nationality | 1.78992  | 0.155126  |       0.0587695  |
| MGR     | Gender      | 0.159741 | 0.690386  |       0.00185401 |
| MGR     | Nationality | 2.13517  | 0.101663  |       0.0693197  |
| MID     | Gender      | 0.1283   | 0.721078  |       0.00148964 |
| MID     | Nationality | 1.15441  | 0.33197   |       0.0387111  |
| SR      | Gender      | 1.29727  | 0.257876  |       0.0148604  |
| SR      | Nationality | 3.26405  | 0.0252466 |       0.102223   |

**Interpretation**

- **Nationality** is significant at p<0.05 for level(s): **SR** (in this dataset: mainly SR).
- **Gender** is not significant within any single level in this mean-score ANOVA (all p>0.05).
- Even where significant, effect sizes (partial η²) are modest, so differences are subtle in raw score units.


---
## 4) Top-K fairness — pooled levels (selection within each run)

|   K |   Total_selected |   Gender_chi2 |    Gender_p |   Gender_selected_F |   Gender_selected_M |   Gender_sel_rate_F |   Gender_sel_rate_M |   Gender_DIR_F_over_M |   Nationality_chi2 |   Nationality_p |   Nat_selected_AL |   Nat_selected_BR |   Nat_selected_IT |   Nat_selected_MO |   Nat_sel_rate_AL |   Nat_sel_rate_BR |   Nat_sel_rate_IT |   Nat_sel_rate_MO |   Nat_DIR_AL_over_IT |   Nat_DIR_BR_over_IT |   Nat_DIR_MO_over_IT |
|----:|-----------------:|--------------:|------------:|--------------------:|--------------------:|--------------------:|--------------------:|----------------------:|-------------------:|----------------:|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|---------------------:|---------------------:|---------------------:|
|   1 |               48 |       48      | 4.26219e-12 |                   0 |                  48 |            0        |            0.25     |              0        |            101.167 |     8.72222e-22 |                 5 |                42 |                 0 |                 1 |         0.0520833 |          0.4375   |         0         |         0.0104167 |            inf       |                  inf |            inf       |
|   3 |              143 |       21.1538 | 4.2385e-06  |                  44 |                  99 |            0.229167 |            0.515625 |              0.444444 |            116.273 |     4.89852e-25 |                46 |                84 |                 4 |                 9 |         0.479167  |          0.875    |         0.0416667 |         0.09375   |             11.5     |                   21 |              2.25    |
|   5 |              239 |       10.046  | 0.00152677  |                  95 |                 144 |            0.494792 |            0.75     |              0.659722 |             61.569 |     2.71621e-13 |                82 |                95 |                19 |                43 |         0.854167  |          0.989583 |         0.197917  |         0.447917  |              4.31579 |                    5 |              2.26316 |

**Interpretation**

- **Definition:** within each run (Job+Level+Version), candidates are ranked by similarity; Top-K are those with rank ≤ K.
- At **Top-1**, the winner is **always male**: 48/48 runs (F: 0).
- Nationality among Top-1 winners is heavily concentrated: BR:42, AL:5, MO:1, IT:0.
- The χ² tests show Top-K selection is **not consistent with equal selection rates** across gender and nationality (very small p-values for K=1/3/5).
- DIR values show large disparities (e.g., F-over-M DIR well below 1 for K=3 and K=5).


---
## 5) Top-K fairness — by hierarchy level

| Level   |   K |   Total_selected |   Gender_chi2 |    Gender_p |   Gender_selected_F |   Gender_selected_M |   Gender_sel_rate_F |   Gender_sel_rate_M |   Gender_DIR_F_over_M |   Nationality_chi2 |   Nationality_p |   Nat_selected_AL |   Nat_selected_BR |   Nat_selected_IT |   Nat_selected_MO |   Nat_sel_rate_AL |   Nat_sel_rate_BR |   Nat_sel_rate_IT |   Nat_sel_rate_MO |   Nat_DIR_AL_over_IT |   Nat_DIR_BR_over_IT |   Nat_DIR_MO_over_IT |
|:--------|----:|-----------------:|--------------:|------------:|--------------------:|--------------------:|--------------------:|--------------------:|----------------------:|-------------------:|----------------:|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|---------------------:|---------------------:|---------------------:|
| JR      |   1 |               12 |      12       | 0.000532006 |                   0 |                  12 |            0        |            0.25     |              0        |            28.6667 |     2.63128e-06 |                 1 |                11 |                 0 |                 0 |         0.0416667 |          0.458333 |         0         |         0         |                  inf |                  inf |                  nan |
| JR      |   3 |               36 |       7.11111 | 0.00766076  |                  10 |                  26 |            0.208333 |            0.541667 |              0.384615 |            27.5556 |     4.50207e-06 |                11 |                21 |                 1 |                 3 |         0.458333  |          0.875    |         0.0416667 |         0.125     |                   11 |                   21 |                    3 |
| MGR     |   1 |               12 |      12       | 0.000532006 |                   0 |                  12 |            0        |            0.25     |              0        |            18      |     0.00043985  |                 3 |                 9 |                 0 |                 0 |         0.125     |          0.375    |         0         |         0         |                  inf |                  inf |                  nan |
| MGR     |   3 |               35 |       4.82857 | 0.0279918   |                  11 |                  24 |            0.229167 |            0.5      |              0.458333 |            30.4857 |     1.09069e-06 |                13 |                20 |                 0 |                 2 |         0.541667  |          0.833333 |         0         |         0.0833333 |                  inf |                  inf |                  inf |
| MID     |   1 |               12 |      12       | 0.000532006 |                   0 |                  12 |            0        |            0.25     |              0        |            28.6667 |     2.63128e-06 |                 0 |                11 |                 0 |                 1 |         0         |          0.458333 |         0         |         0.0416667 |                  nan |                  inf |                  inf |
| MID     |   3 |               36 |       5.44444 | 0.0196307   |                  11 |                  25 |            0.229167 |            0.520833 |              0.44     |            27.1111 |     5.57988e-06 |                 8 |                22 |                 2 |                 4 |         0.333333  |          0.916667 |         0.0833333 |         0.166667  |                    4 |                   11 |                    2 |
| SR      |   1 |               12 |      12       | 0.000532006 |                   0 |                  12 |            0        |            0.25     |              0        |            28.6667 |     2.63128e-06 |                 1 |                11 |                 0 |                 0 |         0.0416667 |          0.458333 |         0         |         0         |                  inf |                  inf |                  nan |
| SR      |   3 |               36 |       4       | 0.0455003   |                  12 |                  24 |            0.25     |            0.5      |              0.5      |            34.8889 |     1.28591e-07 |                14 |                21 |                 1 |                 0 |         0.583333  |          0.875    |         0.0416667 |         0         |                   14 |                   21 |                    0 |

**Interpretation**

- The Top-1 pattern persists **within every level** (JR/MID/MGR/SR): all Top-1 selections are male in each level.
- For Top-3, female selection rates are ~0.21–0.25 while male selection rates are ~0.50–0.54, giving DIR(F/M) ≈ 0.38–0.50 depending on level.
- Nationality disparities also persist by level (IT is rarely selected into Top-K compared to the other nationalities).


---
## 6) Rank-based tests — by level

| Level   |   Gender_MWU_p |   Gender_MWU_U |    Nat_KW_p |   Nat_KW_H |
|:--------|---------------:|---------------:|------------:|-----------:|
| JR      |    0.000187563 |         1658.5 | 9.6544e-13  |    58.9913 |
| MGR     |    0.008406    |         1509.5 | 1.58789e-15 |    72.0051 |
| MID     |    0.00576165  |         1527   | 1.5676e-12  |    58.0055 |
| SR      |    4.64287e-05 |         1704   | 1.41526e-13 |    62.8935 |

**Interpretation**

- These tests operate on **ranks within each run**, so they directly measure who is placed higher/lower in the hiring-style ordering.
- Mann–Whitney U p-values indicate that the **rank distribution differs by gender** in every level (p-values < 0.01 across the board here).
- Kruskal–Wallis p-values indicate that **nationality groups have different rank distributions** within each level (all extremely small p-values).


---
## 7) Paired gender gaps (M − F) — summary across matched pairs

| metric       |        value |
|:-------------|-------------:|
| n_pairs      | 192          |
| mean_diff    |   0.00475156 |
| median_diff  |   0.00455    |
| pct_positive |   0.973958   |
| pct_zero     |   0.00520833 |
| pct_negative |   0.0208333  |

**Interpretation**

- Pairing controls for Job, Level, Version, and Nationality: it compares *the same identity profile* with only gender swapped.
- Mean gap is **0.0048** (M−F), and **97.4%** of pairs favor males.
- Even if the gap is small in absolute score units, its consistency can strongly affect rank-based outcomes (Top-K).


---
## 8) Paired gender gaps (M − F) — by hierarchy level

| Level   |   n |       mean |   median |   pct_positive |
|:--------|----:|-----------:|---------:|---------------:|
| JR      |  48 | 0.00701042 |  0.00705 |       1        |
| MGR     |  48 | 0.00243125 |  0.00215 |       0.958333 |
| MID     |  48 | 0.00329583 |  0.0033  |       0.9375   |
| SR      |  48 | 0.00626875 |  0.00585 |       1        |

**Interpretation**

- The male advantage is present in all levels and is largest (mean gap) in **JR** and **SR** in this dataset.
- In JR and SR, the gap is positive in 100% of matched pairs.


---
## 9) Paired nationality gaps vs IT (within same JD & gender)

| Nationality_vs_IT   |   n_pairs |   mean_diff |   median_diff |   pct_positive |         t_p |   wilcoxon_p |
|:--------------------|----------:|------------:|--------------:|---------------:|------------:|-------------:|
| AL                  |        96 |  0.0160635  |       0.0172  |       0.916667 | 3.42074e-24 |  6.58873e-16 |
| BR                  |        96 |  0.0227521  |       0.02145 |       1        | 2.21861e-36 |  1.77988e-17 |
| MO                  |        96 |  0.00640833 |       0.0073  |       0.75     | 8.86265e-12 |  1.25768e-09 |

**Interpretation**

- Pairing controls for Job, Level, Version, and Gender: it compares nationalities holding everything else constant.
- All three non-IT groups have **higher** similarity scores than IT on average (mean differences > 0).
- BR shows the largest and most consistent advantage over IT; MO shows a smaller advantage.


---
## 10) Robustness across tonality — paired gender gap by version

| Version   |   n |       mean |   median |   pct_positive |
|:----------|----:|-----------:|---------:|---------------:|
| V1        |  64 | 0.0040375  |  0.0042  |       0.921875 |
| V2        |  64 | 0.00603125 |  0.0057  |       1        |
| V3        |  64 | 0.00418594 |  0.00375 |       1        |

**Interpretation**

- The (M−F) gap is **positive in all versions**, meaning the gender pattern is not confined to one writing style.
- V2 shows the largest average gap; V1/V3 are smaller but still consistently positive.


---
## 11) Robustness across tonality — nationality vs IT by version

| Version   | Nat_vs_IT   |   n_pairs |   mean_diff |   pct_positive |   wilcoxon_p |
|:----------|:------------|----------:|------------:|---------------:|-------------:|
| V1        | AL          |        32 |  0.0262687  |        1       |  4.65661e-10 |
| V1        | BR          |        32 |  0.0318344  |        1       |  4.65661e-10 |
| V1        | MO          |        32 |  0.00803437 |        0.8125  |  4.02145e-06 |
| V2        | AL          |        32 |  0.0180438  |        1       |  4.65661e-10 |
| V2        | BR          |        32 |  0.0219344  |        1       |  4.65661e-10 |
| V2        | MO          |        32 |  0.0101844  |        0.90625 |  5.12227e-08 |
| V3        | AL          |        32 |  0.00387812 |        0.75    |  0.00294741  |
| V3        | BR          |        32 |  0.0144875  |        1       |  4.65661e-10 |
| V3        | MO          |        32 |  0.00100625 |        0.53125 |  0.638096    |

**Interpretation**

- AL and BR are consistently above IT across all versions (very small Wilcoxon p-values).
- MO is above IT in V1/V2, but in **V3** the MO–IT difference is not significant (p≈0.64), suggesting this smaller effect is more sensitive to tonality.


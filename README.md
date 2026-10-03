# Marketing A/B Testing Analysis

A statistical analysis of a marketing A/B test designed to evaluate whether showing an advertisement instead of a Public Service Announcement (PSA) affects user conversion.

## Business Objective

Determine whether the marketing advertisement changes the probability that a user makes a purchase compared with the PSA baseline.

## Experiment Design (Pre-Analysis Plan)

> Written before running any outcome analysis. Anything beyond these choices is labeled exploratory.

| Setup Question            | Our Project                                                                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Business goal             | Increase product purchases through the ad campaign                                                                                                    |
| Hypothesis                | If users see the ad instead of the PSA, the conversion rate will change                                                                               |
| Null / Alternative        | H0: p_ad = p_psa. H1: p_ad != p_psa (two-sided, alpha = 0.05)                                                                                         |
| Treatment / Control       | Treatment = `ad`. Control = `psa` (baseline)                                                                                                          |
| Primary metric            | Conversion rate (`converted`), one metric only                                                                                                        |
| Secondary metrics         | Conversion by ad exposure, day, hour (exploratory only)                                                                                               |
| Guardrail metrics         | None available in the dataset (stated as a limitation)                                                                                                |
| Unit of randomization     | User (`user_id`); each user appears once                                                                                                              |
| Pre-planned segments      | Day and hour only; any other cut is exploratory                                                                                                       |
| Statistical test          | Two-proportion z-test (pooled SE), chi-square cross-check, 95% CI (unpooled SE), bootstrap robustness check                                           |
| Multiple comparisons      | Holm correction across all segment tests                                                                                                              |
| Minimum meaningful effect | MPID, set in Phase 5 before interpreting the lift (hypothetical if no business input)                                                                 |
| Decision rule             | Ship if significant, positive, and CI supports an effect above the MPID. Run longer if uncertain. Do not ship if the CI rules out a meaningful effect |

## Project Approach

The analysis is organized into the following phases:

1. **Phase 1 — Setup & Data Preparation**
2. **Phase 2 — Sanity Checks & Descriptive Statistics**
3. **Phase 3 — Hypothesis Testing**
4. **Phase 4 — Effect Size & Confidence Intervals**
5. **Phase 5 — Power & Practical Significance**
6. **Phase 6 — Business Impact**
7. **Phase 7 — Exploratory Segments**
8. **Phase 8 — Final Conclusion**

Confirmatory analysis focuses on the primary conversion-rate comparison. Secondary exposure, day, and hour analyses are exploratory.

## Current Data Status — Phase 1

* Dataset: **588,101 users × 6 columns** after cleaning; no missing values, duplicate rows, or duplicate users.
* Groups: **ad = 564,577, psa = 23,524 (about 24:1)**. Intended allocation unknown, so no SRM test; a balance check is planned in Phase 2.
* `total_ads` is strongly right-skewed (**median 13, mean 24.82, max 2,065**); extreme values were kept because no evidence they are invalid.
* The processed dataset is saved at `data/processed/marketing_ab_clean.csv`.

Detailed phase findings: see `reports/phase_reports/`.

## Project Structure

```text
marketing-ab-testing-analysis/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
│
├── data/
│   ├── raw/
│   │   └── marketing_AB.csv
│   ├── processed/
│   │   └── marketing_ab_clean.csv
│   └── README.md
│
├── notebooks/
│   ├── 01_setup_data_quality.ipynb
│   ├── 02_sanity_checks_descriptives.ipynb
│   ├── 03_hypothesis_test.ipynb
│   ├── 04_effect_size_confidence_intervals.ipynb
│   ├── 05_power_practical_significance.ipynb
│   ├── 06_business_impact.ipynb
│   ├── 07_exploratory_segments.ipynb
│   └── 08_final_conclusion.ipynb
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_prep.py
│   ├── logger.py
│   ├── stats_utils.py
│   └── plot_utils.py
│
├── logs/
│   └── .gitkeep
│
├── reports/
│   ├── figures/
│   ├── tables/
│   ├── phase_reports/
│   │   ├── phase1_findings.md
│   │   └── phase2_findings.md
│   └── executive_summary.md
│
├── tests/
│   ├── test_data_prep.py
│   └── test_stats_utils.py
│
└── dashboard/
    └── looker_studio_link.md
```

## How to Run

1. Download the Kaggle **Marketing A/B Testing** CSV into `data/raw/` (see `data/README.md`).
2. Install dependencies with:

```bash
uv sync
```

3. Run the notebooks in order, from `01` to `08`.

## Results (added after Phase 8)

*To be completed.*

## Limitations (added after Phase 8)

*To be completed.*

## Tech Stack

Python, pandas, NumPy, SciPy, statsmodels, Matplotlib, Seaborn, uv, PyCharm

## Version Control

Repository initialized after Phase 1; one commit per phase.

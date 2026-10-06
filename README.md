# Marketing A/B Testing Analysis

A statistical analysis of a marketing A/B test designed to evaluate whether showing an advertisement instead of a Public Service Announcement (PSA) affects user conversion.

## Business Objective

Determine whether the marketing advertisement changes the probability that a user makes a purchase compared with the PSA baseline.

## Experiment Design (Pre-Analysis Plan)

> Written before running any outcome analysis. Anything beyond these choices is labeled exploratory.

| Setup Question | Our Project |
|---|---|
| Business goal | Increase product purchases through the ad campaign |
| Hypothesis | If users see the ad instead of the PSA, the conversion rate will change |
| Null / Alternative | H0: p_ad = p_psa. H1: p_ad != p_psa (two-sided, alpha = 0.05) |
| Treatment / Control | Treatment = `ad`. Control = `psa` (baseline) |
| Primary metric | Conversion rate (`converted`), one metric only |
| Secondary metrics | Conversion by ad exposure, day, hour (exploratory only) |
| Guardrail metrics | None available in the dataset (stated as a limitation) |
| Unit of randomization | User (`user_id`); each user appears once |
| Pre-planned segments | Day and hour only; any other cut is exploratory |
| Statistical test | Two-proportion z-test (pooled SE), chi-square cross-check, 95% CI (unpooled SE), bootstrap robustness check |
| Multiple comparisons | Holm correction across all segment tests |
| Minimum meaningful effect | MPID, set in Phase 5 before interpreting the lift (hypothetical if no business input) |
| Decision rule | Ship if significant, positive, and CI supports an effect above the MPID. Run longer if uncertain. Do not ship if the CI rules out a meaningful effect |

## Project Approach

The analysis is organized into eight phases. Each phase has its own execution script in `analysis/`, which calls reusable functions from `src/`.

| Phase | Focus | Script |
|---|---|---|
| 1 | Setup & Data Preparation | `analysis/phase1_data_quality.py` |
| 2 | Sanity Checks & Descriptive Statistics | `analysis/phase2_descriptives.py` |
| 3 | Hypothesis Testing | `analysis/phase3_hypothesis_test.py` |
| 4 | Effect Size & Confidence Intervals | `analysis/phase4_effect_size_ci.py` |
| 5 | Power & Practical Significance | `analysis/phase5_power.py` |
| 6 | Business Impact | `analysis/phase6_business_impact.py` |
| 7 | Exploratory Segments | `analysis/phase7_segments.py` |
| 8 | Final Conclusion | `analysis/phase8_final_conclusion.py` |

Confirmatory analysis focuses on the primary conversion-rate comparison. Secondary exposure, day, and hour analyses are exploratory.

**Workflow for each phase:**

```text
analysis/phaseN_*.py
        ↓
src/ reusable functions
        ↓
logs and saved outputs
        ↓
interpretation
        ↓
reports/phase_reports/phaseN_findings.md
```

## Current Status

| Phase | Status |
|---|---|
| 1. Setup & Data Preparation | Complete |
| 2. Sanity Checks & Descriptives | Complete |
| 3. Hypothesis Testing | Next |
| 4. Effect Size & CIs | Pending |
| 5. Power & Practical Significance | Pending |
| 6. Business Impact | Pending |
| 7. Exploratory Segments | Pending |
| 8. Final Conclusion | Pending |

### Phase 1 Summary

- Dataset: **588,101 users × 6 columns** after cleaning; no missing values, duplicate rows, or duplicate users.
- Groups: **ad = 564,577, psa = 23,524 (about 24:1)**. Intended allocation is unknown, so no SRM test was performed.
- `total_ads` is strongly right-skewed (**median 13, mean 24.82, max 2,065**); extreme values were retained because no evidence showed they were invalid.
- The processed dataset is saved at `data/processed/marketing_ab_clean.csv`.

### Phase 2 Summary

- Observed allocation is approximately **96% ad / 4% PSA**. Unequal allocation alone does not establish experiment bias because the intended allocation is unknown.
- Overall conversion rate is **2.5239%**. This is descriptive and does not indicate which group performed better.
- `ad` conversion rate is **2.5547%**, compared with **1.7854%** for `psa`.
- The observed absolute difference is **0.7692 percentage points**, with a **43.09% relative lift**. These are descriptive results and have not yet been tested for statistical significance.
- `most_ads_day` differs statistically between groups: **χ² = 235.6145, df = 6, p < 0.001**.
- `most_ads_hour` differs statistically between groups: **χ² = 192.2917, df = 23, p < 0.001**.
- The day/hour chi-square tests are treated as **plausibility checks, not proof of bias or failed randomization**, because both variables are measured after assignment.
- These findings are documented as a limitation, and Phase 7 segment analyses will be interpreted cautiously.
- The primary experiment analysis is **not ruled out**; Phase 3 proceeds with the planned hypothesis test.

Detailed phase findings: see `reports/phase_reports/`.

## Project Structure

```text
marketing-ab-testing-analysis/
├── README.md
├── LICENSE
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
├── main.py
│
├── data/
│   ├── raw/
│   │   └── marketing_AB.csv          # not committed
│   ├── processed/
│   │   └── marketing_ab_clean.csv
│   └── README.md
│
├── analysis/
│   ├── phase1_data_quality.py
│   ├── phase2_descriptives.py
│   ├── phase3_hypothesis_test.py
│   ├── phase4_effect_size_ci.py
│   ├── phase5_power.py
│   ├── phase6_business_impact.py
│   ├── phase7_segments.py
│   └── phase8_final_conclusion.py
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── logger.py
│   ├── data_prep.py
│   ├── stats_utils.py
│   └── plot_utils.py
│
├── tests/
│   ├── test_data_prep.py
│   └── test_stats_utils.py
│
├── reports/
│   ├── figures/
│   ├── tables/
│   ├── phase_reports/
│   │   ├── phase1_findings.md
│   │   └── phase2_findings.md
│   └── executive_summary.md
│
├── logs/
│   └── .gitkeep
│
├── dashboard/
│   └── looker_studio_link.md
│
└── Project_Decision_Log/
    ├── Phase-1_Decision_Log.md
    └── Phase-2_Decision_Log.md
```

## Project Layout

| Folder / File | Role |
|---|---|
| `README.md` | One-page project overview |
| `analysis/` | Phase-specific execution scripts |
| `src/` | Reusable analytical logic: data preparation, statistics, plotting, logging, and configuration |
| `tests/` | Automated validation of reusable functions |
| `reports/phase_reports/` | Detailed technical findings for each completed phase |
| `reports/tables/` | Saved analytical tables used for review |
| `reports/figures/` | Saved analytical figures |
| `reports/executive_summary.md` | Final one-page summary after Phase 8 |
| `Project_Decision_Log/` | Methodological decisions and reasoning for each phase |
| `main.py` | Simple project entry point |

## How to Run

1. Download the Kaggle **Marketing A/B Testing** CSV into `data/raw/` (see `data/README.md`).
2. Install dependencies:

```bash
uv sync
```

3. Run the phase scripts in order:

```bash
uv run python analysis/phase1_data_quality.py
```

```bash
uv run python analysis/phase2_descriptives.py
```

4. Outputs are saved to the appropriate project directories:
   - Tables → `reports/tables/`
   - Figures → `reports/figures/`
   - Logs → `logs/`
   - Phase findings → `reports/phase_reports/`

## Reproducibility

Analytical parameters are centralized in `src/config.py`:

```text
Random seed       = 42
Significance α    = 0.05
Bootstrap samples = 10,000
```

Dependencies are managed through `pyproject.toml` and locked in `uv.lock`.

## Results (added after Phase 8)

_To be completed._

## Limitations (running list, finalized after Phase 8)

- No date/timestamp column is available, so conversion trends over time and time-based experiment stability cannot be evaluated.
- No revenue, cost, or profit data is available, so the financial/business impact of the campaign cannot be directly quantified.
- Intended group allocation is unknown (observed split is 96% `ad` / 4% `psa`), so an SRM test cannot be performed.
- `most_ads_day` and `most_ads_hour` are measured after assignment; their statistically different distributions are plausibility checks, not proof of biased or successful randomization. Phase 7 segment results will be interpreted cautiously.
- The `psa` group is substantially smaller (23,524 vs 564,577 users), so its baseline conversion rate is estimated less precisely. This is addressed through confidence intervals and power analysis.
- `total_ads` is measured after assignment and is not randomized, so the exposure-conversion relationship is observational and not causal.
- No guardrail metrics are available in the dataset.
- Results apply only to the population and conditions represented in this experiment.

These limitations will be revisited and expanded after the remaining phases.

## Tech Stack

Python, pandas, NumPy, SciPy, statsmodels, Matplotlib, Seaborn, uv, PyCharm

## Version Control

Repository initialized after Phase 1; one commit per phase.
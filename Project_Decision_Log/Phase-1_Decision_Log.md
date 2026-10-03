# PHASE 1: DATA PREPARATION DECISIONS

| # | Finding | Decision | Reason |
|---|---|---|---|
| 1 | `Unnamed: 0` column present | Removed | Exported index column with no analytical meaning |
| 2 | Column names contain spaces | Renamed to snake_case | Consistent, Python-friendly naming |
| 3 | No missing values | No treatment needed | Nothing to fix |
| 4 | No duplicate rows | No removal needed | Nothing to fix |
| 5 | No duplicate `user_id` | User-level uniqueness confirmed | Matches the unit of randomization (one row per user) |
| 6 | Highly unequal allocation (ad 564,577 vs psa 23,524, about 24:1) | Retain all observations | Unequal size alone does not establish bias, and balancing would discard real data |
| 7 | No negative `total_ads` | No correction needed | Values are valid |
| 8 | `most_ads_hour` within 0-23 | No correction needed | Valid 24-hour clock values |
| 9 | `total_ads` strongly right-skewed (median 13, mean 24.82, skewness 7.43) | Retain observations | Skew alone is not an error. Handle it in the exploratory binning |
| 10 | Extreme `total_ads` values (max 2,065) | Retain | No evidence they are invalid or corrupted |
| 11 | Processed dataset | Saved to `data/processed/marketing_ab_clean.csv`, shape 588,101 x 6 | Single clean input for all later phases |
| 12 | Intended allocation ratio unknown | Do not run an SRM test | SRM needs a known intended split |
| 13 | Randomization quality cannot be verified by SRM | Run a day/hour balance check in Phase 2 | Plausibility check only. Both variables are measured after assignment, so it is not proof |
| 14 | Project architecture | Scripts replace notebooks: `analysis/` (phase scripts), `src/` (reusable logic) | Cleaner, testable, and works with the logging system. Trade-off: no inline outputs, so results are saved to `reports/` |
| 15 | Dependency management | `pyproject.toml` and `uv.lock` are the source of truth. No `requirements.txt` | Avoids two files drifting apart |

## Principles applied
- Validation finds problems; cleaning fixes them. The two are kept separate.
- Unusual is not the same as invalid, and unequal is not the same as biased.
- No observation is removed without evidence.
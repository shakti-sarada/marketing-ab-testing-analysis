Phase 1 Findings

1. Data quality

| Item | Result |
|---|---|
| Raw dataset | 588,101 rows, 7 columns |
| Column removed | Unnamed: 0 (exported index) |
| Column renaming | snake_case |
| Prepared dataset | 588,101 rows, 6 analytical columns |

| Validation check | Result |
|---|---|
| Missing values | None |
| Duplicate rows | None |
| Duplicate user_id values | None |
| test_group values | Only expected values: ad and psa |
| converted | Binary |
| total_ads | No negative values |
| most_ads_hour | Valid 0-23 values |
| Observations removed | None (besides the index column) |

No observations were removed because the validation checks did not identify missing, duplicate, or otherwise invalid records.

| Test group | Users |
|---|---:|
| ad | 564,577 |
| psa | 23,524 |
| Ratio (ad:psa) | ~24:1 |

Unequal allocation is noted; intended ratio unknown; SRM not possible; balance check in Phase 2.

2. Distributions

converted

| Value | Count |
|---|---:|
| False | 573,258 |
| True | 14,843 |
| Overall conversion rate | ~2.52% |

This overall rate describes the full dataset and is not an estimate of the difference between the ad and psa groups. The group-specific conversion comparison is part of Phase 2.

most_ads_day

| Item | Day | Count |
|---|---|---:|
| Highest | Friday | 92,608 |
| Second highest | Monday | 87,073 |
| Lowest | Tuesday | 77,479 |

All seven days of the week are represented and no invalid day values were found. These counts describe observed exposure patterns; they do not establish why users had their highest exposure on a particular day.

most_ads_hour

| Statistic | Value |
|---|---:|
| Minimum | 0 |
| Maximum | 23 |
| Mean | ~14.47 |
| Median | 14 |

The range is valid for a 24-hour clock, and the observed highest-exposure hour is centered around the afternoon. The variable represents an hour of day, not the duration of advertising.

3. total_ads upper tail

total_ads is strongly right-skewed.

| Statistic | Value |
|---|---:|
| Mean | 24.82 |
| Median | 13 |
| Skewness | 7.43 |
| 90th percentile | 57 |
| 95th percentile | 88 |
| 99th percentile | 202 |
| 99.5th percentile | 276 |
| 99.9th percentile | ~500 |
| Maximum | 2,065 |

The upper tail contains multiple very high exposure values, including 2,065, 1,778, 1,680, 1,632, and other values above 1,000.

These values are extreme but there is no evidence from the available validation checks that they are invalid or corrupted. No evidence of invalid values was found, so extreme total_ads values were kept.

For later exploratory analysis, total_ads will be treated as a strongly right-skewed exposure variable rather than having extreme observations automatically removed.

A balance check of most_ads_day and most_ads_hour across groups is planned in Phase 2. These variables are measured after assignment, so it is a plausibility check, not proof.
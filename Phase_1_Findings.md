Phase 1 Findings

1. Data quality

The raw Marketing A/B Testing dataset contained 588,101 rows and 7 columns. The exported Unnamed: 0 index column was removed and the remaining columns were renamed to snake_case, producing a prepared dataset with 588,101 rows and 6 analytical columns.

No missing values, duplicate rows, or duplicate user_id values were found. test_group contains the expected ad and psa groups, converted is binary, total_ads contains no negative values, and most_ads_hour contains valid 0–23 hour values.

The group counts are ad = 564,577 and psa = 23,524 (about 24:1). Unequal allocation is noted; intended ratio unknown; SRM not possible; balance check in Phase 2.

The overall conversion count is 14,843 converted users and 573,258 non-converted users, corresponding to an overall conversion rate of approximately 2.52%.

No observations were removed beyond the exported index column because the validation checks did not identify missing, duplicate, or otherwise invalid records.

2. Distributions

Converted

The converted variable contains 573,258 False observations and 14,843 True observations. The overall conversion rate is approximately 2.52%.

This overall rate describes the full dataset and is not an estimate of the difference between the ad and psa groups. The group-specific conversion comparison is part of Phase 2.

most_ads_day

All seven days of the week are represented. Friday has the highest count (92,608), followed by Monday (87,073), while Tuesday has the lowest count (77,479). No invalid day values were found.

These counts describe observed exposure patterns; they do not establish why users had their highest exposure on a particular day.

most_ads_hour

most_ads_hour ranges from 0 to 23, which is valid for a 24-hour clock. The mean is approximately 14.47 and the median is 14, indicating that the observed highest-exposure hour is centered around the afternoon.

The variable represents an hour of day, not the duration of advertising.

3. total_ads upper tail

total_ads is strongly right-skewed. The mean is 24.82 while the median is 13, and skewness is 7.43. Upper-tail inspection showed:

90th percentile = 57

95th percentile = 88

99th percentile = 202

99.5th percentile = 276

99.9th percentile ≈ 500

Maximum = 2,065

The upper tail contains multiple very high exposure values, including 2,065, 1,778, 1,680, 1,632, and other values above 1,000.

These values are extreme but there is no evidence from the available validation checks that they are invalid or corrupted. No evidence of invalid values was found, so extreme total_ads values were kept.

A balance check of most_ads_day and most_ads_hour across groups is planned in Phase 2. These variables are measured after assignment, so it is a plausibility check, not proof.

For later exploratory analysis, total_ads will be treated as a strongly right-skewed exposure variable rather than having extreme observations automatically removed.
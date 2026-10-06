# PHASE 2: SANITY CHECKS & DESCRIPTIVE ANALYSIS DECISIONS

| # | Finding | Decision | Reason |
|---|---|---|---|
| 1 | Observed allocation is `ad = 564,577` and `psa = 23,524` (96% / 4%, approximately 24:1) | Retain all observations | Unequal allocation alone does not establish experimental bias. Intended allocation is unknown. |
| 2 | Intended allocation ratio is unknown | Do not run an SRM test | SRM requires a known intended allocation ratio. |
| 3 | PSA group is much smaller than the ad group | Account for this in later inference | The smaller PSA sample produces less precise estimates and will be considered during confidence interval and power analysis. |
| 4 | Overall conversion rate is 2.5239% | Record as descriptive baseline | Overall conversion combines both groups and cannot determine whether ads performed better than PSA. |
| 5 | Ad conversion rate is 2.5547%; PSA conversion rate is 1.7854% | Carry forward to Phase 3 | This is an observed group difference that requires formal statistical testing. |
| 6 | Observed absolute difference is 0.7692 percentage points | Record as observed treatment effect | It describes the difference in sample conversion rates but does not establish statistical significance or causality. |
| 7 | Observed relative lift is 43.09% | Record as observed relative lift | Relative lift is useful for describing the observed difference but requires statistical inference before drawing conclusions. |
| 8 | `most_ads_day` shows visible differences between groups | Perform formal chi-square plausibility check | Visual inspection alone is insufficient with a large dataset. |
| 9 | Chi-square test for `most_ads_day × test_group`: χ² = 235.6145, df = 6, p < 0.001 | Reject independence hypothesis, but do not label as bias | The distributions differ statistically, but `most_ads_day` is measured after assignment. The result is a plausibility check, not proof of randomization failure. |
| 10 | `most_ads_hour` is between 0 and 23 | Retain values | Values represent valid 24-hour clock hours. |
| 11 | `most_ads_hour` shows some visible percentage differences between groups | Perform a formal chi-square plausibility check | Quantify whether the observed hourly distribution differences are statistically detectable. |
| 12 | `total_ads` mean is approximately 24.8 while median is approximately 12–13 | Retain distribution | Difference between mean and median is consistent with right skewness and is not itself evidence of invalid data. |
| 13 | `total_ads` maximum is 2,065 for ad and 907 for PSA | Retain extreme values | No evidence was found that these observations are invalid or corrupted. |
| 14 | Conversion rate increases with `total_ads` exposure bucket | Keep as exploratory analysis | The relationship is descriptive and does not establish that additional ads cause higher conversion. |
| 15 | `101+` exposure bucket has 16.9051% conversion rate | Do not make a recommendation from this alone | High observed conversion may reflect differences between users receiving different levels of exposure. |
| 16 | Primary conversion comparison has not yet been statistically tested | Defer conclusion | Phase 3 will formally test whether the observed conversion difference is statistically significant. |
| 17 | Descriptive findings cannot establish causality | No causal conclusion in Phase 2 | Observed differences must be supported by appropriate statistical inference before making an experiment decision. |

## Principles applied

- Unequal allocation does not automatically mean bias.
- Intended allocation must be known before performing an SRM test.
- Descriptive differences are not automatically causal effects.
- Statistical significance does not automatically establish experimental bias.
- Post-assignment variables such as `most_ads_day` and `most_ads_hour` should be treated carefully when assessing randomization quality.
- A statistically significant chi-square result is a plausibility check, not proof of randomization failure.
- Unusual or extreme values are not automatically invalid.
- No observations are removed without evidence that they are invalid or corrupted.
- Exploratory relationships are not treated as primary experiment results.
- The primary experiment question remains whether conversion differs between `ad` and `psa`.
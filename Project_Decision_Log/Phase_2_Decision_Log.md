# PHASE 2: SANITY CHECKS & DESCRIPTIVE ANALYSIS DECISIONS

| # | Finding | Decision | Reason |
|---|---|---|---|
| 1 | Overall group allocation is 96% `ad` / 4% `psa` (`ad` = 564,577 vs `psa` = 23,524, about 24:1) | Retain the observed allocation and do not run an SRM test | Intended allocation is unknown, so SRM is not possible; unequal allocation alone does not establish bias |
| 2 | Overall conversion rate is 2.5239% | Treat as descriptive context only | The overall rate combines both groups and cannot determine whether ads outperform PSA |
| 3 | `ad` conversion rate is 2.5547% and `psa` conversion rate is 1.7854% | Record the observed difference as descriptive | The difference must be statistically tested before drawing an inferential conclusion |
| 4 | Absolute conversion-rate difference is 0.7692 percentage points | Record as observed treatment-control difference | It describes the raw difference but does not establish statistical significance or causality by itself |
| 5 | Relative lift is 43.09% | Record as descriptive relative lift | Relative lift communicates the proportional difference but is not evidence of statistical significance by itself |
| 6 | `most_ads_day` distributions showed visible differences between groups | Formally test the day distributions | Visual comparison alone is subjective, especially with a large sample |
| 7 | Chi-square test for `most_ads_day` × `test_group` produced χ² = 235.6145, df = 6, p < 0.001 | Reject the null hypothesis of independence for this descriptive test | The observed day distributions differ statistically between groups |
| 8 | Significant day chi-square result | Do not label the experiment biased | The variables are measured after assignment; the result cannot establish whether randomization itself was unsuccessful |
| 9 | Previous description of day distributions as "roughly similar" | Replace with "visible differences, formally tested, interpreted with caution" | The formal test shows the distributions are statistically different |
| 10 | `most_ads_hour` distributions showed visible differences but broadly similar overall patterns | Formally test the hour distributions | Visual similarity does not establish statistical similarity |
| 11 | Chi-square test for `most_ads_hour` × `test_group` produced χ² = 192.2917, df = 23, p < 0.001 | Reject the null hypothesis of independence for this descriptive test | The observed hourly distributions differ statistically between groups |
| 12 | Significant hour chi-square result | Do not label the experiment biased | `most_ads_hour` is also a post-assignment variable and therefore cannot prove a randomization failure |
| 13 | Day and hour chi-square tests are statistically significant | Record as a limitation and interpret Phase 7 segment analyses cautiously | The distributions differ between groups, but the variables may themselves be affected by assignment |
| 14 | Day/hour balance checks cannot establish randomization success | Treat both tests as plausibility checks, not pass/fail tests | These variables are measured after assignment |
| 15 | Full 24-hour contingency table | Saved to `reports/tables/` | Allows technical reviewers to inspect the complete hourly distribution rather than only selected values |
| 16 | `total_ads` mean is approximately 24.8 in both groups | Treat distributions as broadly similar descriptively | Mean exposure is very close between groups |
| 17 | `total_ads` median is 13 for `ad` and 12 for `psa` | Treat typical exposure as broadly similar | The median number of ads is close between groups |
| 18 | `total_ads` mean substantially exceeds median | Retain right-skew interpretation | The difference indicates a long upper tail |
| 19 | Maximum `total_ads` is 2,065 for `ad` and 907 for `psa` | Retain extreme values | The larger maximum in the `ad` group is partly expected given its much larger sample size, and no evidence of invalidity was found |
| 20 | Conversion rises across `total_ads` exposure buckets | Keep as exploratory analysis | The pattern is descriptive and does not establish that additional ads caused higher conversion |
| 21 | `101+` ads bucket has much higher observed conversion | Do not recommend showing users 101+ ads based on this result | Exposure level is observational here and may be confounded with user behavior |
| 22 | Conversion by exposure, day, and hour | Keep outside the primary confirmatory result | These analyses are secondary/exploratory according to the pre-analysis plan |
| 23 | Phase 2 primary purpose | Complete sanity checks and descriptive analysis before hypothesis testing | Prevents descriptive observations from being confused with inferential conclusions |
| 24 | Primary conversion comparison | Proceed to Phase 3 | The descriptive analysis is complete and the primary statistical test can now be performed without changing the pre-analysis plan |

## Principles applied

- Unequal allocation is not automatically evidence of bias.
- Statistical significance is not the same as experimental bias.
- Post-assignment variables cannot prove successful or failed randomization.
- Descriptive differences are not automatically causal effects.
- Exploratory relationships should not be treated as confirmatory evidence.
- Unusual values are not removed without evidence that they are invalid.
- The primary hypothesis test remains separate from exploratory segment analysis.
- Phase 2 findings are frozen before the primary Phase 3 inference.
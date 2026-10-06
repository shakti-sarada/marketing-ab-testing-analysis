Phase 2 Findings

1. Group allocation

| Test group | Users | Proportion |
|---|---:|---:|
| ad | 564,577 | 96.00% |
| psa | 23,524 | 4.00% |
| Total | 588,101 | 100% |

The allocation is highly unequal (about 24:1), but unequal allocation does not automatically indicate a biased experiment. The intended allocation ratio is unknown, so an SRM test cannot be performed. Unequal allocation is noted; intended ratio unknown; SRM not possible; balance check in Phase 2. The smaller psa group means psa-based estimates will be less precise, which will be considered in Phase 3 and Phase 4.

2. Overall conversion rate

| Metric | Value |
|---|---:|
| Total users | 588,101 |
| Converted | 14,843 |
| Non-converted | 573,258 |
| Overall conversion rate | 2.5239% |

This rate combines the ad and psa groups. It gives baseline context but does not show whether the advertisement was successful.

3. Conversion by test group

| Test group | Users | Conversions | Conversion rate |
|---|---:|---:|---:|
| ad | 564,577 | 14,423 | 2.5547% |
| psa | 23,524 | 420 | 1.7854% |

The ad group has the higher observed conversion rate, by 0.7692 percentage points. This is a descriptive comparison only. It does not establish statistical significance or prove that the advertisement caused the difference. Formal testing is deferred to Phase 3.

4. Balance / plausibility checks

most_ads_day

| Day | ad | psa | Difference (psa - ad), pp |
|---|---:|---:|---:|
| Monday | 14.80% | 14.89% | +0.09 |
| Tuesday | 13.21% | 12.36% | -0.85 |
| Wednesday | 13.71% | 14.84% | +1.13 |
| Thursday | 14.01% | 16.60% | +2.59 |
| Friday | 15.73% | 16.17% | +0.44 |
| Saturday | 13.96% | 12.15% | -1.81 |
| Sunday | 14.58% | 13.00% | -1.58 |

Chi-square test of independence (most_ads_day vs test_group)

| Item | Result |
|---|---|
| H0 | most_ads_day is independent of test_group |
| H1 | most_ads_day is associated with test_group |
| Chi-square statistic | 235.6145 |
| Degrees of freedom | 6 |
| p-value | < 0.001 (displayed as 0.000000) |
| Decision (alpha = 0.05) | Reject H0 |

The most_ads_day distributions differ statistically between groups. The largest gap is Thursday (2.59 percentage points). However, most_ads_day is measured after assignment, so this result is a plausibility check, not proof of bias or randomization failure. The difference could reflect post-assignment user behavior.

most_ads_hour (selected hours)

| Hour | ad | psa | Difference (psa - ad), pp |
|---:|---:|---:|---:|
| 11 | 7.82% | 8.76% | +0.94 |
| 12 | 8.01% | 8.76% | +0.75 |
| 13 | 8.06% | 9.22% | +1.16 |
| 14 | 7.75% | 7.95% | +0.20 |
| 15 | 7.59% | 7.77% | +0.18 |
| 16 | 6.37% | 6.82% | +0.45 |
| 23 | 3.46% | 2.63% | -0.83 |

most_ads_hour ranges from 0 to 23 (valid 24-hour range; mean 14.47, median 14). Hourly patterns are generally similar between groups, with some visible differences. No formal test was run on hours. As a post-assignment variable, any difference would be a plausibility check, not direct evidence of bias.

5. total_ads exposure by group

| Statistic | ad | psa |
|---|---:|---:|
| Users | 564,577 | 23,524 |
| Mean | 24.82 | 24.76 |
| Std. dev. | 43.75 | 42.86 |
| Minimum | 1 | 1 |
| 25th percentile | 4 | 4 |
| Median | 13 | 12 |
| 75th percentile | 27 | 26 |
| Maximum | 2,065 | 907 |

Mean, median, and middle 50% are very similar across groups. In both groups the mean is well above the median, consistent with the strong right-skew found in Phase 1. The maximum differs substantially (2,065 vs 907).

No evidence of invalid values was found, so extreme total_ads values were kept. The distributions are broadly similar, but this does not prove statistical equivalence.

6. Observed treatment effect

| Metric | Result |
|---|---:|
| Ad conversion rate | 2.5547% |
| PSA conversion rate | 1.7854% |
| Absolute difference | 0.7692 percentage points |
| Relative lift | 43.09% over PSA baseline |

The absolute difference and relative lift describe the same observed gap in two ways. Both are descriptive and do not establish statistical significance or causality. Statistical uncertainty will be evaluated in Phase 3 and confidence intervals in Phase 4.

7. Conversion by ad exposure

Because total_ads is strongly right-skewed, exposure was grouped into buckets:

| Ad exposure | Users | Conversions | Conversion rate |
|---|---:|---:|---:|
| 1-5 | 177,823 | 449 | 0.2525% |
| 6-10 | 82,952 | 409 | 0.4931% |
| 11-20 | 127,484 | 1,070 | 0.8393% |
| 21-50 | 130,776 | 3,774 | 2.8859% |
| 51-100 | 46,002 | 5,242 | 11.3952% |
| 101+ | 23,064 | 3,899 | 16.9051% |

Conversion rate increases consistently across exposure buckets, from 0.2525% in the lowest bucket to 16.9051% in the highest. This is a strong descriptive association between observed exposure and conversion.

It does not establish that more ad exposure causes higher conversion. total_ads is an observed post-assignment variable, not the randomized treatment, and users with different exposure levels may differ in other ways. This analysis is exploratory and is not used as the primary experiment decision. The high conversion rate at 101+ ads does not justify recommending 101+ ads without further causal evidence.

8. Phase 2 conclusion

| Item | Result |
|---|---|
| Allocation | ~96% ad / 4% psa; intended ratio unknown, SRM not testable |
| most_ads_day balance | Differs statistically (chi-square 235.6145, df 6, p < 0.001); plausibility check only, not proof of bias |
| most_ads_hour balance | Generally similar, some visible differences; not formally tested |
| total_ads balance | Broadly similar; right-skewed; extreme values kept |
| Overall conversion rate | 2.5239% |
| ad vs psa conversion | 2.5547% vs 1.7854% |
| Absolute difference | 0.7692 percentage points |
| Relative lift | 43.09% |
| Exposure-conversion association | Strong, exploratory, not causal |
| Observations removed | None |

All results are descriptive or plausibility checks. No observations were removed based on the Phase 2 sanity checks. The observed conversion difference is sufficiently defined to proceed to Phase 3 (Hypothesis Testing), using the pre-specified two-proportion z-test with a pooled standard error and the planned chi-square cross-check.
PHASE 1 — DATA PREPARATION DECISIONS

1. Removed `Unnamed: 0`
   Reason:
   Exported dataframe/index column with no analytical meaning.

2. Renamed columns to snake_case
   Reason:
   Consistent Python-friendly naming convention.

3. No missing values found
   Decision:
   No missing-value treatment required.

4. No duplicate rows found
   Decision:
   No duplicate-row removal required.

5. No duplicate user IDs found
   Decision:
   User-level uniqueness requirement satisfied.

6. Highly unequal experimental allocation
   Decision:
   Retain all observations. Do not assume unequal allocation means bias
   or invalid experimentation.

7. No negative total_ads values
   Decision:
   No correction required.

8. most_ads_hour is within 0–23
   Decision:
   No correction required.

9. total_ads is strongly right-skewed
   Decision:
   Retain observations. Do not automatically remove extreme values.

10. Extreme total_ads observations
    Decision:
    Retain because no evidence of invalid/corrupted observations was found.

11. Processed dataset
    Output:
    data/processed/marketing_ab_clean.csv
    Shape:
    588,101 × 6
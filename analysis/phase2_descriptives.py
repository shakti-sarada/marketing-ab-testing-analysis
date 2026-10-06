"""
Phase 2: Sanity Checks & Descriptive Analysis

Step 2.1:
Inspect the observed allocation between the ad and PSA groups.
"""

import pandas as pd
from scipy.stats import chi2_contingency
from src.data_prep import load_processed_data


def main():
    print("=" * 60)
    print("PHASE 2: SANITY CHECKS & DESCRIPTIVE ANALYSIS")
    print("=" * 60)

    # ------------------------------------------------------------
    # Step 2.1: Group Allocation
    # ------------------------------------------------------------

    df = load_processed_data()

    group_counts = df["test_group"].value_counts()

    print("\nGroup Allocation:")
    print(group_counts.to_dict())

    print("\nGroup Proportions:")
    print(df["test_group"].value_counts(normalize=True).to_dict())


    # ------------------------------------------------------------
    # Step 2.2: Overall Conversion Rate
    # ------------------------------------------------------------

    total_users = len(df)
    converted_users = int(df["converted"].sum())

    overall_conversion_rate = (
        converted_users / total_users
    )

    print("\nOverall Conversion:")
    print(f"Total users: {total_users:,}")
    print(f"Converted users: {converted_users:,}")
    print(
        f"Overall conversion rate: "
        f"{overall_conversion_rate:.4%}"
    )

    # ------------------------------------------------------------
    # Step 2.3: Conversion Rate by Test Group
    # ------------------------------------------------------------

    group_summary = (
        df.groupby("test_group")["converted"]
        .agg(
            users="count",
            conversions="sum",
        )
    )

    group_summary["conversion_rate"] = (
        group_summary["conversions"]
        / group_summary["users"]
    )

    print("\nConversion by Test Group:")
    print(group_summary)

    # ============================================================
    # Step 2.4A: most_ads_day by Test Group
    # ============================================================

    day_distribution = pd.crosstab(
        df["most_ads_day"],
        df["test_group"],
    )

    print("\nMost Ads Day by Test Group:")
    print(day_distribution)

    # ------------------------------------------------------------
    # Within-group percentages
    # ------------------------------------------------------------

    day_distribution_pct = (
            pd.crosstab(
                df["most_ads_day"],
                df["test_group"],
                normalize="columns",
            )
            * 100
    )

    print("\nMost Ads Day by Test Group (%):")
    print(day_distribution_pct.round(2))

    # ============================================================
    # Step 2.4B: most_ads_hour by Test Group
    # ============================================================

    hour_distribution_pct = (
            pd.crosstab(
                df["most_ads_hour"],
                df["test_group"],
                normalize="columns",
            )
            * 100
    )

    print("\nMost Ads Hour by Test Group (%):")
    print(hour_distribution_pct.round(2))

    # ------------------------------------------------------------
    # Step 2.5: total_ads by Test Group
    # ------------------------------------------------------------

    ads_by_group = (
        df.groupby("test_group")["total_ads"]
        .describe()
    )

    print("\nTotal Ads by Test Group:")
    print(ads_by_group)


    # ------------------------------------------------------------
    # Step 2.6: Observed Treatment Effect
    # ------------------------------------------------------------

    ad_rate = group_summary.loc["ad", "conversion_rate"]
    psa_rate = group_summary.loc["psa", "conversion_rate"]

    absolute_difference = ad_rate - psa_rate

    relative_lift = (
        absolute_difference / psa_rate
    )

    print("\nObserved Treatment Effect:")
    print(
        f"Ad conversion rate: "
        f"{ad_rate:.4%}"
    )

    print(
        f"PSA conversion rate: "
        f"{psa_rate:.4%}"
    )

    print(
        f"Absolute difference: "
        f"{absolute_difference:.4%}"
    )

    print(
        f"Absolute difference (percentage points): "
        f"{absolute_difference * 100:.4f}"
    )

    print(
        f"Relative lift: "
        f"{relative_lift:.2%}"
    )

    # ------------------------------------------------------------
    # Step 2.7: Conversion by Ad Exposure
    # ------------------------------------------------------------

    df["ads_exposure_bucket"] = pd.cut(
        df["total_ads"],
        bins=[0, 5, 10, 20, 50, 100, float("inf")],
        labels=[
            "1-5",
            "6-10",
            "11-20",
            "21-50",
            "51-100",
            "101+",
        ],
        include_lowest=True,
    )

    exposure_summary = (
        df.groupby(
            "ads_exposure_bucket",
            observed=False,
        )["converted"]
        .agg(
            users="count",
            conversions="sum",
        )
    )

    exposure_summary["conversion_rate"] = (
        exposure_summary["conversions"]
        / exposure_summary["users"]
    )

    print("\nConversion by Ad Exposure:")
    print(exposure_summary)

    # ============================================================
    # Chi-Square Test: most_ads_day vs test_group
    # ============================================================

    day_table = pd.crosstab(
        df["most_ads_day"],
        df["test_group"]
    )

    print("\nMost Ads Day × Test Group:")
    print(day_table)

    chi2, p_value, dof, expected = chi2_contingency(day_table)

    print("\nChi-Square Test: most_ads_day vs test_group")
    print(f"Chi-square statistic: {chi2:.4f}")
    print(f"Degrees of freedom: {dof}")
    print(f"p-value: {p_value:.6f}")


if __name__ == "__main__":
    main()
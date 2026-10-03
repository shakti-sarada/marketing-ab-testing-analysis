"""
Phase 1: Setup & Data Quality

This script executes the complete Phase 1 workflow:
1. Load the raw dataset
2. Prepare/clean column names
3. Validate data quality
4. Inspect distributions
5. Inspect the upper tail of total_ads
6. Save the processed dataset
"""

from src.data_prep import (
    load_raw_data,
    prepare_columns,
    validate_data,
    inspect_distributions,
    inspect_total_ads_tail,
    save_processed_data,
)


def main():
    # ============================================================
    # Phase 1 — Setup & Data Quality
    # ============================================================

    print("=" * 60)
    print("PHASE 1: SETUP & DATA QUALITY")
    print("=" * 60)

    # ------------------------------------------------------------
    # Step 1: Load raw dataset
    # ------------------------------------------------------------

    df = load_raw_data()

    # ------------------------------------------------------------
    # Step 2: Prepare dataset
    # ------------------------------------------------------------

    df = prepare_columns(df)

    # ------------------------------------------------------------
    # Step 3: Validate data quality
    # ------------------------------------------------------------

    validate_data(df)

    # ------------------------------------------------------------
    # Step 4: Inspect distributions
    # ------------------------------------------------------------

    inspect_distributions(df)

    # ------------------------------------------------------------
    # Step 5: Inspect total_ads upper tail
    # ------------------------------------------------------------

    inspect_total_ads_tail(df)

    # ------------------------------------------------------------
    # Step 6: Save processed dataset
    # ------------------------------------------------------------

    save_processed_data(df)

    print("=" * 60)
    print("PHASE 1 COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
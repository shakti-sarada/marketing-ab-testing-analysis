from src.data_prep import (
    load_raw_data,
    prepare_columns,
    save_processed_data,
    load_processed_data,
)


# ============================================================
# Load and Prepare Dataset
# ============================================================

df = load_raw_data()

df = prepare_columns(df)


# ============================================================
# Save Processed Dataset
# ============================================================

df1 = load_processed_data()
df1
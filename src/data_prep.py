import pandas as pd

from src.config import RAW_DATA_PATH,PROCESSED_DATA_PATH
from src.logger import get_logger


logger = get_logger(__name__)


COLUMN_RENAME_MAP = {
    "user id": "user_id",
    "test group": "test_group",
    "total ads": "total_ads",
    "most ads day": "most_ads_day",
    "most ads hour": "most_ads_hour",
}


def load_raw_data() -> pd.DataFrame:
    """
    Load the raw Marketing A/B Testing dataset.

    Returns
    -------
    pd.DataFrame
        Raw dataset loaded from the configured CSV path.
    """

    logger.info("Starting raw dataset loading.")
    logger.info("Reading dataset from: %s", RAW_DATA_PATH)

    try:
        df = pd.read_csv(RAW_DATA_PATH)

        logger.info(
            "Raw dataset loaded successfully. Shape: %s",
            df.shape,
        )

        logger.info(
            "Columns detected: %s",
            list(df.columns),
        )

        return df

    except FileNotFoundError:
        logger.error(
            "Raw dataset not found at: %s",
            RAW_DATA_PATH,
        )
        raise

    except Exception:
        logger.exception("Unexpected error while loading the raw dataset.")
        raise


def prepare_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove the exported index column and rename dataset columns
    using snake_case.

    Parameters
    ----------
    df : pd.DataFrame
        Raw Marketing A/B Testing dataset.

    Returns
    -------
    pd.DataFrame
        Dataset with prepared column names.
    """

    logger.info("Starting column preparation.")

    df = df.copy()

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])
        logger.info("Dropped exported index column: 'Unnamed: 0'.")

    df = df.rename(columns=COLUMN_RENAME_MAP)

    logger.info(
        "Columns renamed successfully: %s",
        list(df.columns),
    )

    return df

def validate_data(df: pd.DataFrame) -> dict:
    """
    Perform structural and integrity checks on the prepared dataset.

    The function reports potential data-quality issues but does not
    modify or remove any observations.

    Parameters
    ----------
    df : pd.DataFrame
        Prepared Marketing A/B Testing dataset.

    Returns
    -------
    dict
        Collection of validation results.
    """

    logger.info("Starting data quality validation.")

    results = {}

    # --------------------------------------------------------
    # Shape
    # --------------------------------------------------------

    results["shape"] = df.shape

    logger.info("Dataset shape: %s", df.shape)

    # --------------------------------------------------------
    # Data types
    # --------------------------------------------------------

    results["dtypes"] = df.dtypes.astype(str).to_dict()

    logger.info("Data types checked.")

    # --------------------------------------------------------
    # Missing values
    # --------------------------------------------------------

    missing_values = df.isna().sum()

    results["missing_values"] = missing_values.to_dict()

    logger.info(
        "Total missing values: %d",
        int(missing_values.sum()),
    )

    # --------------------------------------------------------
    # Duplicate rows
    # --------------------------------------------------------

    duplicate_rows = int(df.duplicated().sum())

    results["duplicate_rows"] = duplicate_rows

    logger.info(
        "Duplicate rows: %d",
        duplicate_rows,
    )

    # --------------------------------------------------------
    # Duplicate users
    # --------------------------------------------------------

    duplicate_user_rows = int(df["user_id"].duplicated().sum())

    results["duplicate_user_rows"] = duplicate_user_rows

    logger.info(
        "Duplicate user_id rows: %d",
        duplicate_user_rows,
    )

    # --------------------------------------------------------
    # Test groups
    # --------------------------------------------------------

    test_groups = df["test_group"].value_counts(dropna=False)

    results["test_groups"] = test_groups.to_dict()

    logger.info(
        "Test group values: %s",
        test_groups.to_dict(),
    )

    # --------------------------------------------------------
    # Converted values
    # --------------------------------------------------------

    converted_values = df["converted"].value_counts(dropna=False)

    results["converted_values"] = converted_values.to_dict()

    logger.info(
        "Converted values: %s",
        converted_values.to_dict(),
    )

    # --------------------------------------------------------
    # Numeric validity
    # --------------------------------------------------------

    results["negative_total_ads"] = int(
        (df["total_ads"] < 0).sum()
    )

    results["invalid_hours"] = int(
        (~df["most_ads_hour"].between(0, 23)).sum()
    )

    logger.info(
        "Negative total_ads values: %d",
        results["negative_total_ads"],
    )

    logger.info(
        "Invalid most_ads_hour values: %d",
        results["invalid_hours"],
    )

    logger.info("Data quality validation completed.")

    return results

def inspect_distributions(df: pd.DataFrame) -> dict:
    """
    Inspect categorical and numeric distributions without modifying
    the dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Prepared Marketing A/B Testing dataset.

    Returns
    -------
    dict
        Distribution summaries for key variables.
    """

    logger.info("Starting distribution inspection.")

    results = {}

    # --------------------------------------------------------
    # Categorical variables
    # --------------------------------------------------------

    results["test_group"] = df["test_group"].value_counts(
        dropna=False
    ).to_dict()

    results["converted"] = df["converted"].value_counts(
        dropna=False
    ).to_dict()

    results["most_ads_day"] = df["most_ads_day"].value_counts(
        dropna=False
    ).to_dict()

    # --------------------------------------------------------
    # Numeric variables
    # --------------------------------------------------------

    results["most_ads_hour"] = df["most_ads_hour"].describe().to_dict()

    results["total_ads"] = df["total_ads"].describe().to_dict()

    results["total_ads_skewness"] = df["total_ads"].skew()

    logger.info(
        "Unique test groups: %d",
        df["test_group"].nunique(),
    )

    logger.info(
        "Unique most_ads_day values: %d",
        df["most_ads_day"].nunique(),
    )

    logger.info(
        "total_ads mean: %.2f",
        df["total_ads"].mean(),
    )

    logger.info(
        "total_ads median: %.2f",
        df["total_ads"].median(),
    )

    logger.info(
        "total_ads skewness: %.2f",
        df["total_ads"].skew(),
    )

    logger.info("Distribution inspection completed.")

    return results

def inspect_total_ads_tail(df: pd.DataFrame) -> dict:
    """
    Inspect the upper tail of total_ads without modifying the dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Prepared Marketing A/B Testing dataset.

    Returns
    -------
    dict
        Summary statistics for the upper tail of total_ads.
    """

    logger.info("Starting total_ads upper-tail inspection.")

    quantiles = df["total_ads"].quantile(
        [0.90, 0.95, 0.99, 0.995, 0.999]
    )

    top_values = (
        df["total_ads"]
        .sort_values(ascending=False)
        .head(20)
        .tolist()
    )

    results = {
        "quantiles": quantiles.to_dict(),
        "top_values": top_values,
    }

    logger.info(
        "total_ads upper quantiles: %s",
        results["quantiles"],
    )

    logger.info(
        "Top 20 total_ads values: %s",
        results["top_values"],
    )

    logger.info("total_ads upper-tail inspection completed.")

    return results

def save_processed_data(df: pd.DataFrame) -> None:
    """
    Save the prepared dataset to the configured processed-data path.

    Parameters
    ----------
    df : pd.DataFrame
        Prepared Marketing A/B Testing dataset.
    """

    logger.info(
        "Saving processed dataset to: %s",
        PROCESSED_DATA_PATH,
    )

    PROCESSED_DATA_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        PROCESSED_DATA_PATH,
        index=False,
    )

    logger.info(
        "Processed dataset saved successfully. Shape: %s",
        df.shape,
    )
    
def load_processed_data() -> pd.DataFrame:
    """
    Load the prepared Marketing A/B Testing dataset.

    Returns
    -------
    pd.DataFrame
        Processed dataset loaded from the configured CSV path.
    """
    logger.info("Starting processed dataset loading.")
    logger.info(
        "Reading processed dataset from: %s",
        PROCESSED_DATA_PATH,
    )

    try:
        df = pd.read_csv(PROCESSED_DATA_PATH)

        logger.info(
            "Processed dataset loaded successfully. Shape: %s",
            df.shape,
        )

        logger.info(
            "Processed columns detected: %s",
            list(df.columns),
        )

        return df

    except FileNotFoundError:
        logger.error(
            "Processed dataset not found at: %s",
            PROCESSED_DATA_PATH,
        )
        raise

    except Exception:
        logger.exception(
            "Unexpected error while loading the processed dataset."
        )
        raise
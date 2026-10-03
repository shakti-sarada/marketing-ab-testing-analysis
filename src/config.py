from pathlib import Path


# ============================================================
# Project Paths
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
TABLES_DIR = REPORTS_DIR / "tables"

LOGS_DIR = PROJECT_ROOT / "logs"


# ============================================================
# Data Paths
# ============================================================

RAW_DATA_PATH = RAW_DATA_DIR / "marketing_AB.csv"
PROCESSED_DATA_PATH = PROCESSED_DATA_DIR / "marketing_ab_clean.csv"


# ============================================================
# Statistical Configuration
# ============================================================

RANDOM_SEED = 42

ALPHA = 0.05

BOOTSTRAP_RESAMPLES = 10_000
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent


DIRECTORIES = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src",
    "logs",
    "reports/figures",
    "reports/tables",
    "tests",
    "dashboard",
]


FILES = [
    "README.md",
    "requirements.txt",
    ".gitignore",
    "LICENSE",
    "data/README.md",
    "src/__init__.py",
    "src/config.py",
    "src/logger.py",
    "src/data_prep.py",
    "src/stats_utils.py",
    "src/plot_utils.py",
    "logs/.gitkeep",
    "tests/test_stats_utils.py",
    "dashboard/looker_studio_link.md",
]


NOTEBOOKS = [
    "01_setup_data_quality.ipynb",
    "02_sanity_checks_descriptives.ipynb",
    "03_hypothesis_test.ipynb",
    "04_effect_size_confidence_intervals.ipynb",
    "05_power_practical_significance.ipynb",
    "06_business_impact.ipynb",
    "07_exploratory_segments.ipynb",
    "08_final_conclusion.ipynb",
]


def create_directories():
    for directory in DIRECTORIES:
        path = PROJECT_ROOT / directory
        path.mkdir(parents=True, exist_ok=True)
        print(f"[DIR]   {path.relative_to(PROJECT_ROOT)}")


def create_files():
    for file in FILES:
        path = PROJECT_ROOT / file
        path.parent.mkdir(parents=True, exist_ok=True)

        if not path.exists():
            path.touch()
            print(f"[FILE]  {path.relative_to(PROJECT_ROOT)}")
        else:
            print(f"[SKIP]  {path.relative_to(PROJECT_ROOT)} already exists")


def create_notebooks():
    notebooks_dir = PROJECT_ROOT / "notebooks"

    for notebook in NOTEBOOKS:
        path = notebooks_dir / notebook

        if not path.exists():
            path.write_text(
                '{"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}',
                encoding="utf-8",
            )
            print(f"[NOTEBOOK] {path.relative_to(PROJECT_ROOT)}")
        else:
            print(f"[SKIP]     {path.relative_to(PROJECT_ROOT)} already exists")


def main():
    print("\nCreating Marketing A/B Testing project structure...\n")

    create_directories()
    create_files()
    create_notebooks()

    print("\nProject structure created successfully.")


if __name__ == "__main__":
    main()
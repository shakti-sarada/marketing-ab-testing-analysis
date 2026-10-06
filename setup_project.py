from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

DIRECTORIES = [
    "data/raw",
    "data/processed",
    "analysis",
    "src",
    "tests",
    "reports/figures",
    "reports/tables",
    "reports/phase_reports",
    "logs",
    "dashboard",
    "Project_Decision_Log",
]

# Files created empty if missing.
# pyproject.toml, uv.lock and .python-version are created by uv, so they are not listed here.
FILES = [
    "README.md",
    "LICENSE",
    "data/README.md",
    "src/__init__.py",
    "src/config.py",
    "src/logger.py",
    "src/data_prep.py",
    "src/stats_utils.py",
    "src/plot_utils.py",
    "tests/test_data_prep.py",
    "tests/test_stats_utils.py",
    "reports/phase_reports/phase1_findings.md",
    "reports/executive_summary.md",
    "Project_Decision_Log/Phase_1_Decision_Log.md",
    "dashboard/looker_studio_link.md",
    "logs/.gitkeep",
    "main.py",
]

# Files that get starter content when they are created.
FILES_WITH_CONTENT = {
    ".gitignore": (
        "data/raw/*.csv\n"
        "logs/*.log\n"
        ".venv/\n"
        "__pycache__/\n"
        ".ipynb_checkpoints/\n"
        ".env\n"
        ".idea/\n"
    ),
}

# One stub per phase. Each holds only a docstring until the phase starts.
PHASE_SCRIPTS = {
    "phase1_data_quality.py": "Phase 1: setup and data quality.",
    "phase2_descriptives.py": "Phase 2: sanity checks and descriptive statistics.",
    "phase3_hypothesis_test.py": "Phase 3: hypothesis testing.",
    "phase4_effect_size_ci.py": "Phase 4: effect size and confidence intervals.",
    "phase5_power.py": "Phase 5: power and practical significance.",
    "phase6_business_impact.py": "Phase 6: business impact.",
    "phase7_segments.py": "Phase 7: exploratory segments.",
    "phase8_final_conclusion.py": "Phase 8: final conclusion.",
}


def create_directories():
    for directory in DIRECTORIES:
        path = PROJECT_ROOT / directory
        path.mkdir(parents=True, exist_ok=True)
        print(f"[DIR]   {path.relative_to(PROJECT_ROOT)}")


def create_files():
    for file in FILES:
        path = PROJECT_ROOT / file
        path.parent.mkdir(parents=True, exist_ok=True)

        if path.exists():
            print(f"[SKIP]  {path.relative_to(PROJECT_ROOT)} already exists")
        else:
            path.touch()
            print(f"[FILE]  {path.relative_to(PROJECT_ROOT)}")


def create_files_with_content():
    for file, content in FILES_WITH_CONTENT.items():
        path = PROJECT_ROOT / file

        if path.exists():
            print(f"[SKIP]  {path.relative_to(PROJECT_ROOT)} already exists")
        else:
            path.write_text(content, encoding="utf-8")
            print(f"[FILE]  {path.relative_to(PROJECT_ROOT)}")


def create_phase_scripts():
    analysis_dir = PROJECT_ROOT / "analysis"

    for script, description in PHASE_SCRIPTS.items():
        path = analysis_dir / script

        if path.exists():
            print(f"[SKIP]  {path.relative_to(PROJECT_ROOT)} already exists")
        else:
            path.write_text(
                f'"""{description} Stub: implement when this phase starts."""\n',
                encoding="utf-8",
            )
            print(f"[PHASE] {path.relative_to(PROJECT_ROOT)}")


def main():
    print("\nCreating Marketing A/B Testing project structure...\n")

    create_directories()
    create_files()
    create_files_with_content()
    create_phase_scripts()

    print("\nProject structure created successfully.")


if __name__ == "__main__":
    main()
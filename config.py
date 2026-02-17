from pathlib import Path

# =========================
# Scraping configuration
# =========================

SCRAPERS = {
    "workua": {
        "enabled": True,
        "delay": 1.0,
        "max_concurrent": 5,
    },
    "dou": {
        "enabled": True,
        "delay": 1.0,
        "max_concurrent": 5,
    },
}

MAX_VACANCIES_PER_SOURCE = 200  # safety limit

# =========================
# Technologies (can be removed later)
# =========================

KNOWN_TECHS = {
    "python", "django", "flask", "fastapi",
    "react", "vue", "angular",
    "docker", "kubernetes",
    "postgresql", "mysql", "sqlite", "redis",
    "aws", "gcp", "azure",
    "git", "linux",
    "html", "css", "javascript", "typescript",
    "graphql", "rest", "api",
    "celery", "pandas", "numpy", "scipy",
}

# =========================
# Paths
# =========================

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
HISTORY_DIR = DATA_DIR / "history"

REPORTS_DIR = BASE_DIR / "reports"
IMAGES_DIR = REPORTS_DIR / "images"

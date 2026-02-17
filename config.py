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

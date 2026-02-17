import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)


def save_json(data: List[Dict], filename: str | None = None) -> Path:
    if not filename:
        filename = f"vacancies_{datetime.now().date()}.json"

    path = DATA_DIR / filename

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return path

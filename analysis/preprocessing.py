import json
import re
from pathlib import Path
from typing import Dict
import pandas as pd


def load_raw_data(data_dir: Path) -> pd.DataFrame:
    if not data_dir.is_dir():
        raise ValueError(f"{data_dir} is not a directory")

    records = []

    for file in data_dir.glob("*.json"):
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

            if isinstance(data, list):
                records.extend(data)
            else:
                records.append(data)

    return pd.DataFrame(records)


def normalize_text(text: str) -> str:
    if not text:
        return ""

    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s\+#]", " ", text)

    return text.strip()


def preprocess_vacancy(vacancy: Dict) -> Dict:
    vacancy["description_normalized"] = normalize_text(
        vacancy.get("description", "")
    )
    vacancy["title_normalized"] = normalize_text(
        vacancy.get("title", "")
    )
    return vacancy

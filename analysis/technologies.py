from collections import Counter
import pandas as pd
from config import KNOWN_TECHS


def extract_technologies_from_text(text: str) -> list[str]:
    if not text:
        return []

    text_lower = text.lower()
    detected = []

    for tech in KNOWN_TECHS:
        if tech in text_lower:
            detected.append(tech)

    return detected


def extract_technologies(df: pd.DataFrame) -> Counter:
    counter = Counter()

    for tech_list in df["technologies"].dropna():
        if not isinstance(tech_list, list):
            continue

        for tech in tech_list:
            tech = tech.strip()
            if tech and tech in KNOWN_TECHS:
                counter[tech] += 1

    return counter


def counter_to_df(counter: Counter) -> pd.DataFrame:
    return (
        pd.DataFrame(counter.items(), columns=["technology", "count"])
        .sort_values("count", ascending=False)
    )


def technologies_by_experience(
        df: pd.DataFrame,
        experience_level: str
) -> Counter:
    subset = df[
        (df["experience_level"] == experience_level)
    ]

    counter = Counter()
    for tech_list in subset["technologies"].dropna():
        if not isinstance(tech_list, list):
            continue

        for tech in tech_list:
            tech = tech.strip()
            if tech and tech in KNOWN_TECHS:
                counter[tech] += 1

    return counter

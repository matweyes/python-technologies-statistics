import re


def extract_years(text: str) -> int | None:
    match = re.search(r"(\d+)\+?\s*(year|years|рок)", text)
    return int(match.group(1)) if match else None


def classify_experience(text: str) -> str:
    if not isinstance(text, str):
        return "unknown"

    text = text.lower()

    if re.search(r"\b(0|1)\+?\s*(year|рок|рік)", text) or "junior" in text:
        return "junior"

    if re.search(r"\b(2|3)\+?\s*(year|рок)", text) or "middle" in text:
        return "middle"

    if re.search(r"\b(4|5|6|7)\+?\s*(year|рок)", text) or "senior" in text:
        return "senior"

    return "unknown"

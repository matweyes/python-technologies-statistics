from bs4 import BeautifulSoup


def parse_html(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, "lxml")


def get_text_safe(element) -> str:
    return element.get_text(strip=True) if element else ""


def get_int_safe(text: str | None) -> int | None:
    if not text:
        return None
    digits = "".join(filter(str.isdigit, text))
    return int(digits) if digits else None

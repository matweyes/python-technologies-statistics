from typing import List, Dict
import aiohttp

from scraper.base import BaseScraper
from scraper.parser import parse_html, get_text_safe


class DOUScraper(BaseScraper):
    BASE_URL = "https://jobs.dou.ua/vacancies/?category=Python"

    async def get_vacancy_links(
            self,
            session: aiohttp.ClientSession
    ) -> List[str]:
        html = await self.fetch(session, self.BASE_URL)
        soup = parse_html(html)

        links = set()
        for tag in soup.select("li.l-vacancy a.vt"):
            href = tag.get("href")
            if href:
                links.add(href)

        return list(links)

    async def scrape_vacancy(
            self,
            session: aiohttp.ClientSession,
            url: str
    ) -> Dict:
        html = await self.fetch(session, url)
        soup = parse_html(html)

        return {
            "source": "dou.ua",
            "url": url,
            "title": get_text_safe(soup.select_one("h1")),
            "company": get_text_safe(soup.select_one("div.b-compinfo div.l-n a")),
            "description": get_text_safe(soup.select_one(".vacancy-section")),
        }

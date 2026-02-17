from typing import List, Dict
import aiohttp

from scraper.base import BaseScraper
from scraper.parser import parse_html, get_text_safe


class WorkUAScraper(BaseScraper):
    BASE_URL = "https://www.work.ua/jobs-python/"

    async def get_vacancy_links(
            self,
            session: aiohttp.ClientSession
    ) -> List[str]:
        html = await self.fetch(session, self.BASE_URL)
        soup = parse_html(html)

        links = set()
        for tag in soup.select("div.job-link h2 a"):
            href = tag.get("href")
            if href:
                links.add(f"https://www.work.ua{href}")

        return list(links)

    async def scrape_vacancy(
            self,
            session: aiohttp.ClientSession,
            url: str
    ) -> Dict:
        html = await self.fetch(session, url)
        soup = parse_html(html)

        technologies = [
            li.get_text(strip=True).lower()
            for li in soup.select("div.wordwrap ul.flex li")
        ]

        return {
            "source": "work.ua",
            "url": url,
            "title": get_text_safe(soup.select_one("h1")),
            "company": get_text_safe(
                soup.select_one("div.wordwrap ul.list-unstyled li.text-indent a.inline span")
            ),
            "description": get_text_safe(soup.select_one("div.wordwrap")),
            "technologies": technologies  # store as list, not string
        }

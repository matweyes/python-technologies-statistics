import asyncio
import aiohttp
from abc import ABC, abstractmethod
from typing import List, Dict


class BaseScraper(ABC):
    BASE_URL: str = ""

    def __init__(
            self,
            delay: float = 1.0,
            max_concurrent: int = 5,
    ):
        self.delay = delay
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (JobMarketAnalyzer/1.0)"
        }

    async def fetch(self, session: aiohttp.ClientSession, url: str) -> str:
        async with self.semaphore:
            await asyncio.sleep(self.delay)
            async with session.get(
                    url,
                    headers=self.headers,
                    timeout=20
            ) as response:
                response.raise_for_status()
                return await response.text()

    @abstractmethod
    async def get_vacancy_links(
            self,
            session: aiohttp.ClientSession
    ) -> List[str]:
        pass

    @abstractmethod
    async def scrape_vacancy(
            self,
            session: aiohttp.ClientSession,
            url: str
    ) -> Dict:
        pass

    async def scrape_all(self) -> List[Dict]:
        async with aiohttp.ClientSession() as session:
            links = await self.get_vacancy_links(session)

            tasks = [
                self.scrape_vacancy(session, link)
                for link in links
            ]

            results = []
            for coro in asyncio.as_completed(tasks):
                try:
                    data = await coro
                    if data:
                        results.append(data)
                except Exception as e:
                    print(f"[ERROR] {e}")

            return results

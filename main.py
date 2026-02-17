import asyncio
from datetime import datetime

from scraper import WorkUAScraper, DOUScraper
from scraper.saver import save_json
from config import SCRAPERS, MAX_VACANCIES_PER_SOURCE, RAW_DATA_DIR, HISTORY_DIR, IMAGES_DIR


async def run_scraper(name: str):
    if name == "workua":
        cfg = SCRAPERS["workua"]
        scraper = WorkUAScraper(
            delay=cfg["delay"],
            max_concurrent=cfg["max_concurrent"],
        )
    elif name == "dou":
        cfg = SCRAPERS["dou"]
        scraper = DOUScraper(
            delay=cfg["delay"],
            max_concurrent=cfg["max_concurrent"],
        )
    else:
        raise ValueError(f"Unknown scraper: {name}")

    print(f"[START] {name}")
    data = await scraper.scrape_all()

    if MAX_VACANCIES_PER_SOURCE:
        data = data[:MAX_VACANCIES_PER_SOURCE]

    print(f"[DONE] {name}: {len(data)} vacancies")
    return name, data


async def main():
    tasks = []

    for scraper_name, cfg in SCRAPERS.items():
        if cfg["enabled"]:
            tasks.append(run_scraper(scraper_name))

    results = await asyncio.gather(*tasks)

    all_data = {}
    for name, data in results:
        all_data[name] = data

        save_json(
            data,
            filename=f"{name}_{datetime.now().date()}.json"
        )

    # combined snapshot (for analysis)
    merged = [
        vacancy
        for source in all_data.values()
        for vacancy in source
    ]

    save_json(
        merged,
        filename=f"all_sources_{datetime.now().date()}.json"
    )

    print(f"[TOTAL] {len(merged)} vacancies scraped")


if __name__ == "__main__":
    for path in [
        RAW_DATA_DIR,
        HISTORY_DIR,
        IMAGES_DIR,
    ]:
        path.mkdir(parents=True, exist_ok=True)

    asyncio.run(main())

# Tech Market Demand Analyzer (Python)

## Project Overview

This project is an **async web scraping & data analysis pipeline** that collects Python-related job vacancies from public job boards and analyzes the **most demanded technologies on the tech market**.

The main goal is to help developers:

* understand which technologies are currently in demand
* compare requirements for **Junior / Middle / Senior** positions
* observe technology trends based on real job market data

The project intentionally separates **Scraping** and **Analysis** logic, following SRP and clean architecture principles.

---

## Data Sources

The project currently scrapes **publicly available information** from:

* **Work.ua** – provides structured technology lists
* **DOU.ua** – provides unstructured job descriptions

> ⚠️ Disclaimer: Only public data is scraped. No authentication, private data, or restricted content is accessed.

---

## Project Structure

```
project/
├── scraper/                 # Async web scrapers (data collection)
│   ├── base.py              # Base async scraper
│   ├── workua.py            # Work.ua scraper
│   ├── dou.py               # DOU.ua scraper
│   ├── parser.py            # HTML parsing helpers
│   └── saver.py             # Save raw data to JSON
│
├── analysis/                # Data analysis logic
│   ├── preprocessing.py     # Data loading & normalization
│   ├── technologies.py      # Technology extraction & counters
│   ├── experience.py        # Experience level classification
│   └── visualization.py     # Charts & plots
│
├── data/                    # Raw scraped JSON files
├── reports/
│   └── images/              # Generated diagrams
│
├── notebooks/
│   └── 01_data_preview_and_analysis.ipynb
│
├── config.py                # Configuration (paths, tech lists, etc.)
├── main.py                  # Async runner
└── README.md
```

---

## Technologies Used

* **Python 3.13**
* **aiohttp** – async HTTP requests
* **BeautifulSoup (bs4)** – HTML parsing
* **pandas** – data manipulation
* **matplotlib** – visualization
* **Jupyter Notebook** – interactive analysis

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone git@github.com:matweyes/python-technologies-statistics.git
cd python-technologies-statistics
```

### 2. Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run linter

```bash
flake8 --exclude=.venv,data,reports,notebooks .
```

### 4. Run async scraping

```bash
python main.py
```

This will:

* scrape vacancies from Work.ua and DOU.ua
* save raw data into the `data/` directory

### 5. Run analysis & visualization

Open Jupyter Notebook:

```bash
jupyter notebook
```

Then open:

```
notebooks/01_data_preview_and_analysis.ipynb
```

This notebook:

* loads scraped data
* preprocesses and normalizes it
* builds statistics for technologies and experience levels
* generates charts in `reports/images/`

---

## Analysis Logic

### Experience Levels

Vacancies are classified into:

* `junior`
* `middle`
* `senior`

Based on keywords and years of experience mentioned in job descriptions.

### Technology Extraction

* **Work.ua**: technologies are extracted from structured HTML lists
* **DOU.ua**: technologies are extracted from job descriptions using keyword-based text analysis

This approach allows:

* unified analysis across multiple sources
* extension to new job boards

---

## Example Outputs

Generated charts include:

* Top technologies overall
* Top technologies for Junior / Middle / Senior roles
* Experience level distribution

All charts are saved in:

```
reports/images/
```

---

## Key Takeaways

* Real-world job data is often **inconsistent and unstructured**
* Separating scraping and analysis simplifies debugging and scaling
* Defensive data processing is essential for reliable insights

---

## Legal Notice

This project is created for **educational purposes only**.

All scraped data:

* is publicly available
* is used in aggregated form
* is not stored or redistributed for commercial use

---

## Author

**@matweyes**

Python Developer

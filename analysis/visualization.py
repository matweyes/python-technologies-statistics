import re
import matplotlib.pyplot as plt
from typing import Dict
from collections import Counter
from pathlib import Path
from config import IMAGES_DIR

CYRILLIC_RE = re.compile(r'[\u0400-\u04FF]')


def plot_top_technologies(tech_stats: Dict[str, int], top_n: int = 10):
    items = sorted(
        tech_stats.items(),
        key=lambda x: x[1],
        reverse=True
    )[:top_n]

    labels, values = zip(*items)

    plt.figure()
    plt.bar(labels, values)
    plt.xticks(rotation=45, ha="right")
    plt.title("Top Technologies Demand")
    plt.tight_layout()

    path = IMAGES_DIR / "top_technologies.png"
    plt.savefig(path)
    plt.close()

    return path


def plot_experience_distribution(exp_stats: Dict[str, int]):
    labels = exp_stats.keys()
    values = exp_stats.values()

    plt.figure()
    plt.bar(labels, values)
    plt.title("Experience Level Distribution")
    plt.tight_layout()

    path = IMAGES_DIR / "experience_distribution.png"
    plt.savefig(path)
    plt.close()

    return path


def plot_trends(trend_data: Dict[str, Dict[str, int]]):
    for date, stats in trend_data.items():
        for tech, count in stats.items():
            plt.plot(date, count, marker="o", label=tech)

    plt.legend()
    plt.title("Technology Trends Over Time")
    plt.tight_layout()

    path = IMAGES_DIR / "technology_trends.png"
    plt.savefig(path)
    plt.close()

    return path


def plot_counter(
        counter: Counter,
        title: str,
        output_path: Path | None = None,
        top_n: int = 10
) -> None:
    """
    Plot a horizontal bar chart from a Counter.
    """
    if not isinstance(counter, Counter):
        raise TypeError(f"Expected Counter, got {type(counter)}")

    counter = Counter({
        tech: count
        for tech, count in counter.items()
        if not CYRILLIC_RE.search(tech)
    })

    if len(counter) == 0:
        raise ValueError("Counter is empty — nothing to plot")

    items = counter.most_common(top_n)
    labels, values = zip(*items)

    plt.figure(figsize=(8, 5))
    plt.barh(labels, values)
    plt.gca().invert_yaxis()
    plt.title(title)
    plt.tight_layout()

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=150)
        plt.close()
    else:
        plt.show()

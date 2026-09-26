"""Generate the website chart with Python and Matplotlib (pip install matplotlib)."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# EgoThumb paper, Table I: demonstrator evaluated in the training task areas.
TASKS = ["Pick Up\nCube", "Unscrew\nCap", "Stir\nTea", "Transfer\nBall"]
SUCCESS_RATES = [100, 70, 90, 100]
OUTPUT = Path(__file__).resolve().parents[1] / "assets/media/images/demo_performance.svg"


def main():
    plt.rcParams.update({"font.size": 14, "font.family": "DejaVu Sans", "svg.hashsalt": "egothumb-demo"})
    fig, ax = plt.subplots(figsize=(8, 4.4), layout="constrained")
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")
    bars = ax.bar(TASKS, SUCCESS_RATES, width=0.55, color="#52778c", zorder=3)
    ax.bar_label(bars, labels=[f"{rate}%" for rate in SUCCESS_RATES], padding=7, fontsize=16, color="#293b4d", weight="bold")
    ax.set_ylim(0, 114)
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.yaxis.set_major_formatter(PercentFormatter(100))
    ax.set_ylabel("Success rate", color="#293b4d", labelpad=12)
    ax.grid(axis="y", color="#dfe5ea", linewidth=0.8, zorder=0)
    ax.tick_params(axis="both", length=0, pad=10, colors="#425466")
    for spine in ax.spines.values():
        spine.set_visible(False)
    fig.savefig(OUTPUT, transparent=True, metadata={
        "Date": None,
        "Title": "Demonstrator performance",
        "Description": "Table I, demonstrator: Pick Up Cube 100%; Unscrew Cap 70%; Stir Tea 90%; Transfer Ball 100%. Average 90%.",
    })
    plt.close(fig)


if __name__ == "__main__":
    main()

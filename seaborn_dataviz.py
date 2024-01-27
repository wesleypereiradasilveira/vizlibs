from matplotlib.axes import Axes
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def line_chart(data: pd.DataFrame) -> None:
    plot = sns.lineplot(data)    
    plot.set_title("Amostragem")
    plot.set_ylabel("Label Y")
    plot.set_xlabel("Label X")

    plt.show()

def bar_chart(data: pd.DataFrame) -> None:
    sns.barplot(
        data,
        x="Fruits",
        y="Quantities"
    )

    plt.show()

def hist_chart(data: pd.DataFrame) -> None:
    plot = sns.histplot(
        data, 
        bins=8, 
        linewidth=0.5, 
        edgecolor="white", 
        legend=False
    )

    plt.show()
    save_chart(plot, "hist_chart.png")

def save_chart(plot: Axes, filename: str) -> None:
    image_dir = Path.cwd() / "images" / filename
    plot.get_figure().savefig(image_dir)

def main():
    # data = {
    #     "Amostra_A": [1, 2, 3, 4],
    #     "Amostra_B": [2, 4, 6, 8],
    #     "Amostra_C": [4, 8, 12, 16],
    # }
    # index = [1, 2, 3, 4]

    # df = pd.DataFrame(data, index)
    # line_chart(df)

    # data = {
    #     "Fruits": ["Orange", "Watermelon", "Mango", "Jackfruit"],
    #     "Quantities": [60, 100, 85, 30]
    # }

    # df = pd.DataFrame(data)
    # bar_chart(df)

    research = np.random.normal(170, 10, 250)
    df = pd.DataFrame(data=research)
    hist_chart(df)

if __name__ == "__main__":
    main()

from matplotlib.axes import Axes
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def line_chart(data: pd.DataFrame) -> None:
    data.plot.line(
        title="Amostragem com Pandas",
        ylabel="Label Y",
        xlabel="Label X"
    )
    
    plt.show()

def bar_chart(data: pd.DataFrame) -> None:
    data.plot.bar(
        x="Fruits",
        y="Quantities",
        rot=0,
        title="Amostragem com Pandas",
    )

    plt.show()

def hist_chart(data: pd.DataFrame) -> None:
    data.plot.hist(
        bins=8,
        linewidth=0.5,
        edgecolor="white",
        title="Amostragem com Pandas",
        legend=False,
        ylabel=""
    )

    plt.show()

def pie_chart(data: pd.DataFrame) -> None:
    plot = data.plot.pie(
        y="Percentages",
        legend=False,
        ylabel="",
        autopct="%1.2f%%"
    )

    plt.show()
    save_chart("pandas_pie_chart", "png", plot)

def save_chart(filename: str, extension: str, plot: Axes) -> None:
    image_dir = Path.cwd() / "images" / f"{filename}.{extension}"
    plot.get_figure().savefig(image_dir)

def main():
    # data = {
    #     "sample_A": [1, 2, 3, 4],
    #     "sample_B": [2, 4, 6, 8],
    #     "sample_C": [4, 8, 12, 16]
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

    # research = np.random.normal(170, 10, 250)
    # df = pd.DataFrame(data=research)
    # hist_chart(df)

    data = {
        "Percentages": [15, 30, 45, 10]
    }
    index = ["Oranges", "Watermelon", "Mango", "Jackfruit"]

    df = pd.DataFrame(data, index)
    pie_chart(df)

if __name__ == "__main__":
    main()

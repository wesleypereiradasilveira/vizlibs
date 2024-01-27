from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def line_graph() -> Figure:
    fig, ax = plt.subplots(1, 2)

    index = [1,2,3,4]

    sample_a = [1,4,2,3]
    sample_b = [2,8,4,6]

    ax[0].plot(index, sample_a, label="Amostra A", color="red", marker="o")

    ax[0].set_title("Amostragem A")
    ax[0].set_ylabel("Label Y")
    ax[0].set_xlabel("Label X")
    ax[0].legend()

    ax[1].plot(index, sample_b, label="Amostra B", color="green", marker="o")

    ax[1].set_title("Amostragem B")
    ax[1].set_xlabel("Label X")
    ax[1].set_ylabel("Label Y")
    ax[1].legend()

    plt.show()
    return fig

def bar_graph() -> Figure:
    figure, graphs = plt.subplots()

    fruits = ["Orange", "Watermelon", "Mango", "Jackfruit"]
    quantities = [60, 100, 85, 30]

    graphs.bar(fruits, quantities, label="Quantidade de Frutas")
    graphs.set_xlabel("Frutas")
    graphs.legend()

    plt.show()
    return figure

def hist_graph() -> Figure:
    figure, graphs = plt.subplots()

    research = np.random.normal(170, 10, 250)
    graphs.hist(research, bins=8, linewidth=0.5, edgecolor="white")

    plt.show()
    return figure

def pie_graph() -> Figure:
    figure, graphs = plt.subplots()

    labels = ["Grape", "Strawberry", "Pineapple", "Papaya"]
    percentages = [15, 30, 45, 10]

    graphs.pie(percentages, labels=labels, autopct="%1.2f%%")

    plt.show()
    return figure

def main():
    figure = line_graph()
    image_dir = Path.cwd() / "images" / f"{line_graph.__name__}.png"

    figure.savefig(image_dir, dpi=150, bbox_inches="tight")

if __name__ == "__main__":
    main()

import bokeh.plotting as bkh
import numpy as np
import pandas as pd
from math import pi
from pathlib import Path
from bokeh.transform import cumsum

def line_chart(x: list, y: list):
    fig = bkh.figure(
        title="Amostra com Bokeh",
        x_axis_label="Label X",
        y_axis_label="Label Y"
    )
    fig.line(x, y[0], color="blue", line_width=1, legend_label="Sample A")
    fig.line(x, y[1], color="red", line_width=1, legend_label="Sample B")
    fig.line(x, y[2], color="orange", line_width=1, legend_label="Sample C")

    bkh.output_file(Path.cwd() / "images" / "line_chart.html")
    bkh.show(fig)

def hist_chart(narray: np.ndarray):
    hist, edges = np.histogram(narray, density=True, bins=8)
    fig = bkh.figure()
    fig.quad(
        top=hist,
        bottom=0,
        left=edges[:-1],
        right=edges[1:],
        line_color="white"
    )

    bkh.output_file(Path.cwd() / "images" / "hist_chart.html")
    bkh.show(fig)

def pie_chart(data: pd.DataFrame):
    fig = bkh.figure(
        height=350,
        title="Amostra com Bokeh",
        toolbar_location=None,
        tools="hover",
        tooltips="@fruits: @value%",
        x_range=(-0.5, 1.0)
    )
    fig.wedge(
        x=0,
        y=1,
        radius=0.4,
        start_angle=cumsum("angle", include_zero=True),
        end_angle=cumsum("angle"),
        line_color="white",
        fill_color="color",
        legend_field="fruits",
        source=data
    )
    fig.axis.axis_label = None
    fig.axis.visible = False
    fig.grid.grid_line_color = None

    bkh.output_file(Path.cwd() / "images" / "pie_chart.html")
    bkh.show(fig)

def bar_chart(x: list[str], y: list[int], colors: list[str]):
    fig = bkh.figure(
        title="Amostra",
        x_axis_label="Label X",
        y_axis_label="Label Y",
        x_range=x,
        width=1024,
        height=768,
    )
    fig.vbar(
        x=x,
        top=y,
        legend_label="quantities",
        width=0.5,
        bottom=0,
        fill_color=colors
    )

    fig.axis.axis_label = None
    fig.legend.visible = False
    fig.grid.grid_line_color = None

    bkh.output_file(Path.cwd() / "images" / "bar_chart.html")
    bkh.show(fig)

def main() -> None:
    # index = [1, 2, 3, 4]
    # sample_a = [1, 2, 3, 4]
    # sample_b = [2, 4, 6, 8]
    # sample_c = [4, 8, 12, 16]

    # line_chart(x=index, y=[sample_a, sample_b, sample_c])

    # research = np.random.normal(170, 10, 250)
    # hist_chart(research)

    # x = {
    #     "Grape": 15,
    #     "Strawberry": 30,
    #     "Pineapple": 45,
    #     "Papaya": 10
    # }
    # data = pd.Series(x).reset_index(name="value").rename(columns={"index": "fruits"})
    # data["angle"] = data["value"] / data["value"].sum() * 2 * pi
    # data["color"] = ["purple", "red", "orange", "yellow"]

    # pie_chart(data)

    fruits = ["Orange", "Watermelon", "Mango", "Jackfruit"]
    quantities = [60, 100, 85, 30]
    colors = ["Orange", "Green", "Red", "Yellow"]

    bar_chart(fruits, quantities, colors)

if __name__ == "__main__":
    main()

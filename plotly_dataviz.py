import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio
from pathlib import Path

def line_chart(index: list[int], samples: list[list]):
    fig = px.line(
        x=index, 
        y=samples,
        title="Amostra com Plotly",
        labels=dict(value="Label Y", x="Label X", variable="samples")
    )
    fig.data[0].name="Amostra A"
    fig.data[1].name="Amostra B"
    fig.data[2].name="Amostra C"
    fig.update_layout(showlegend=False)
    fig.show(
        config=dict(displayModeBar=False)
    )

def bar_chart(index: list[str], data: list[int]):
    fig = px.bar(
        x=index,
        y=data,
        title="Amostra com Plotly",
        color=index,
        labels=dict(y="Label Y", x="Label X", color="Fruits")
    )

    fig.show()

def hist_chart(data: np.ndarray):
    fig = px.histogram(
        data,
        nbins=8,
        title="Amostra com Plotly"
    )
    fig.update_layout(showlegend=False)
    fig.update_xaxes(title_text="Label X")
    fig.update_yaxes(title_text="Label Y")
    fig.update_traces(marker_line_width=0.5, marker_line_color="white")

    fig.show()

    # image_dir = Path.cwd() / "images" / "plotly_hist_chart.png"
    # pio.write_image(fig, image_dir, format="png")

def pie_chart(data: pd.DataFrame):
    fig = px.pie(
        data,
        values="Percentages",
        names="Fruits",
    )
    fig.update_layout(showlegend=False)
    fig.update_traces(textinfo="percent+label")
    fig.update_layout(hovermode=False)

    fig.show()

def main():
    # index = [1, 2, 3, 4]
    # samples = [
    #     [1, 4, 2, 3],
    #     [2, 8, 4, 6],
    #     [4, 16, 8, 12]
    # ]
    # line_chart(index, samples)

    # fruits = ["Orange", "Watermelon", "Mango", "Jackfruit"]
    # quantities = [60, 100, 85, 30]
    # bar_chart(fruits, quantities)

    research = np.random.normal(170, 10, 250)
    hist_chart(research)

    # data = {
    #     "Fruits": ["Orange", "Watermelon", "Mango", "Jackfruit"],
    #     "Percentages": [15, 30, 45, 10]
    # }
    # df = pd.DataFrame(data)
    # pie_chart(df)

if __name__ == "__main__":
    main()

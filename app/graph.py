from altair import Chart, X, Y, Color, Tooltip
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    chart = Chart(df).mark_circle(size=60).encode(
        x=X(x),
        y=Y(y),
        color=Color(target),
        tooltip=Tooltip(df.columns.tolist())
    ).properties(
        width=600,
        height=400,
        title=f"{y} by {x} for {target}"
    )
    return chart

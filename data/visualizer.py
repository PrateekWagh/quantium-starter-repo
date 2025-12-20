import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

df = pd.read_csv("Soul_Foods_Data.csv", parse_dates=["date"])

df.sort_values("date")
fig = px.line(df, x="date", y="Sales", title="Pink Morsel Performance")
fig.update_layout(xaxis_title="Date", yaxis_title="Sales(£)")

app = Dash()
app.layout = html.Div(children=[html.H1("Soul Foods Visualiser"),
                                dcc.Graph(id="pink_morsel_graph", figure=fig)
                                ])


if __name__ == "__main__":
    app.run(debug=True)

    import pandas as pd

    price_change_date = pd.to_datetime("2021-01-15")


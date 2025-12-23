import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, callback, Output, Input

df = pd.read_csv("Soul_Foods_Data.csv")
app = Dash()
app.layout = html.Div(children=[html.H1("Soul Foods Visualiser"),
                                html.Br(),
                                html.H1("For looking at the specific report of different regions."),
                                html.Div(children=dcc.RadioItems([{'label':'East Region', 'value':'east'},
                                                                  {'label':'West Region', 'value':'west'},
                                                                  {'label':'North Region', 'value':'north'},
                                                                  {'label':'South Region', 'value':'south'},
                                                                  {'label':'Overall Performance', 'value':'Overall Performance'}
                                                                  ], inline=True, value="east", id="my-input")),
                                html.Br(),
                                html.Div(id="my-output"),
                                dcc.Graph(id="pink_morsel_graph"),


                                ])

@callback(
    Output(component_id='pink_morsel_graph', component_property="figure"),
    Input(component_id='my-input', component_property='value')
)

def update_output(selected_region):
    if selected_region != "Overall Performance":
        filtered_df = df[df["region"] == selected_region]
    else:
        filtered_df = df

    fig = px.line(filtered_df, x="date", y="Sales", title=f"Pink Morsel Performance - {selected_region.upper()}")
    fig.update_layout(xaxis_title="Date", yaxis_title="Sales(£)")



    return fig





if __name__ == "__main__":
    app.run(debug=True)



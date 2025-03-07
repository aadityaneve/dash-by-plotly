# dcc => Dash Core Components
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

# Initialize the app
app = Dash()

# App Layout
# app.layout = [
#     html.Div(
#         children="My First App with Data, Graph, and Controls.",
#         style={"textAlign": "center"},
#     ),
#     html.Hr(),
#     dcc.RadioItems(
#         id="controls-and-radio-items",
#         options=["pop", "lifeExp", "gdpPercap"],
#         value="lifeExp",
#         style={"display": "flex"},
#     ),
#     dcc.Graph(
#         id="graph-content",
#         figure=px.histogram(
#             df,
#             x="continent",
#             y="lifeExp",
#             color="continent",
#             histfunc="avg",
#             labels={"lifeExp": "Life Expectancy", "continent": "Continent"},
#             title="Histogram",
#         ),
#     ),
#     dash_table.DataTable(data=df.to_dict("records"), page_size=10),
# ]


app.layout = [
    html.Div(
        children="My First App with Data, Graph, and Controls.",
        style={"textAlign": "center"},
    ),
    html.Hr(),
    dcc.RadioItems(
        id="controls-and-radio-items",
        options=["pop", "lifeExp", "gdpPercap"],
        value="lifeExp",
        style={"display": "flex"},
    ),
    dcc.Graph(
        id="graph-content",
        figure=px.histogram(
            df,
            x="continent",
            y="lifeExp",
            color="continent",
            histfunc="avg",
            labels={"lifeExp": "Life Expectancy", "continent": "Continent"},
            title="Histogram",
        ),
    ),
    dash_table.DataTable(data=df.to_dict("records"), page_size=10),
]

# print("IIIIIIIIII ============= ", df.head(5))

# Add controls to build the interactions
@callback(
    Output(component_id="graph-content", component_property="figure"),
    Input(component_id="controls-and-radio-items", component_property="value"),
)
def update_graph(col_chosen):
    print("VLUEEEEEEEEEEE ====", col_chosen)
    fig = px.histogram(
        df,
        x="continent",
        y=col_chosen,
        histfunc="avg",
        labels={"lifeExp": "Life Expectancy", "continent": "Continent"},
        title="Histogram",
    )
    return fig


# Run the app
if __name__ == "__main__":
    app.run(debug=True)

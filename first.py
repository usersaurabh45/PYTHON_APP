from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load dataset
df = px.data.iris()

# Create Dash app
app = Dash(__name__)

# Dashboard layout
app.layout = html.Div([
    html.H1("Iris Flower Analysis Dashboard"),

    html.Label("Select Flower Species"),

    dcc.Dropdown(
        id="species_dropdown",
        options=[
            {"label": "Setosa", "value": "setosa"},
            {"label": "Versicolor", "value": "versicolor"},
            {"label": "Virginica", "value": "virginica"},
        ],
        value="setosa",
        clearable=False,
    ),

    dcc.Graph(id="species_graph")
])


# Callback
@app.callback(
    Output(component_id="species_graph", component_property="figure"),
    Input(component_id="species_dropdown", component_property="value")
)
def update_graph(species):

    filtered_df = df[df["species"] == species]

    fig = px.scatter(
        filtered_df,
        x="sepal_width",
        y="sepal_length",
        color="species",
        title=f"Iris Analysis: {species}"
    )

    return fig


# Run application
if __name__ == "__main__":
    app.run(debug=True)
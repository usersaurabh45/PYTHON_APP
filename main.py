from dash import Dash,html
app=Dash(__name__)
app.layout = html.Div([
    html.H1("Welcom to the Python Dashboard"),
    html.P("MY First Interactive Dashboard"),
    html.H2("Learning Dash Framework")
])
if __name__=="__main__":
    app.run(debug=True)

from dash import dash, html


def create_dash_app():
    """
    A function to create the dash app.

    :return:
    """

    app = dash.Dash(__name__)

    app.layout = html.Div([
        html.H1('Sample Dash Page'),
    ], className="container")

    return app

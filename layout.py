from dash import Dash, html, dcc

app = Dash(__name__)

side_panel_layout = html.Div(
    id="panel-side",
    children=[
        html.Div(id="app-name", children="Agata Lis Portfolio"),
        html.P(" "),
        html.P("The projects are being prepared"),
        dcc.Link(href='https://github.com/isdatarael/PortfolioApp', target="_blank",
                 children='See the application source code',
                 style={'color': 'white', 'marigin-top': 15}),
    ],
)
main_panel_layout = html.Div(
    id="panel-upper-lower",
    children=[
        html.H3("Content available soon"),
        html.Div(
            id="panel",
            children=[
                html.Div(
                    id="panel-lower",
                    children=[
                        html.Div(
                            id="panel-lower-0",
                            children=[],
                        ),
                        html.Div(
                            id="panel-lower-1",
                            children=[
                                html.Div(
                                    id="panel-lower-led-displays",
                                    children=[],
                                ),
                                html.Div(
                                    id="panel-lower-indicators",
                                    children=[
                                        html.Div(
                                            id="panel-lower-indicators-0",
                                            children=[],
                                        ),
                                        html.Div(
                                            id="panel-lower-indicators-1",
                                            children=[],
                                        ),
                                        html.Div(
                                            id="panel-lower-indicators-2",
                                            children=[],
                                        ),
                                    ],
                                ),
                                html.Div(
                                    id="panel-lower-graduated-bars",
                                    children=[],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)

root_layout = html.Div(
    id="root",
    children=[
        dcc.Store(id="store-placeholder"),
        dcc.Store(
            id="store-data",
            data={
                },
        ),
        side_panel_layout,
        main_panel_layout,
    ],
)
from dash import Dash, html, dcc

import layout

app = Dash(__name__)

app.layout = layout.root_layout
app.title = 'Agata Lis Portfolio'

if __name__ == '__main__':
    app.run_server(debug=True)
import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, 'https://codepen.io/chriddyp/pen/bWLwgP.css'],
                assets_folder="static",
                assets_url_path="static",
                meta_tags=[
                    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
                ],
                suppress_callback_exceptions=True,
                )

app.title = "GradeCalc"

server = app.server

application = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

login_layout = html.Div(
    dbc.Card(dbc.CardHeader("Login page"))
)

create_account_layout = html.Div(

)

select_class_layout = html.Div(

)

enter_grades_layout = html.Div(

)

grade_view_layout = html.Div(

)

page_not_found = html.Div(
    dbc.Card(dbc.CardHeader("Sorry, couldn't find that page"))
)



@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/login':
        return login_layout
    elif pathname == '/':
        return login_layout
    elif pathname == '/create-account':
        return create_account_layout
    elif pathname == '/select-class':
        return select_class_layout
    elif pathname == '/enter-grades':
        return enter_grades_layout
    elif pathname == '/grade-view':
        return grade_view_layout
    else:
        return page_not_found


if __name__ == '__main__':
    app.run_server(debug=True)
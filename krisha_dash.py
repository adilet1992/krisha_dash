import dash
import dash_core_components as dcc
import dash_html_components as html

districts = ['Алатауский', 'Алмалинский', 'Ауэзовский', 'Бостандыкский', 'Жетысуский', 'Медеуский', 'Наурызбайский', 'Турксибский']
materials = ['кирпичный', 'монолитный', 'панельный']
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1('Узнайте цену квартир в Алматы', style={'font-family': 'Arial', 'text-align': 'center', 'margin-bottom': '50px'}),
        html.H3('Выберите район:', style={'font-family': 'Arial', 'text-align': 'center'}),
        dcc.Dropdown(
            options=[
                {'label': district, 'value': district} for district in districts
                ],
            multi=False,
            value=districts[0],
            style={'width': '400px', 'font-family': 'Arial', 'margin': 'auto'},
            clearable=False
        ),
        html.H3('Выберите тип постройки:', style={'font-family': 'Arial', 'text-align': 'center'}),
        dcc.Dropdown(
            options=[
                {'label': material, 'value': material} for material in materials
            ],
            multi=False,
            value=materials[0],
            style={'width': '400px', 'margin': 'auto', 'font-family': 'Arial'},
            clearable=False
        ),
        html.H3('Площадь квартиры:', style={'font-family': 'Arial', 'text-align': 'center'}),
        dcc.Input(
            placeholder='Площадь квартиры',
            type='number',
            value=40,
            style={'width': '200px', 'margin-left': '660px'},
            min=15,
            max=500,
            required=True
        ),
        html.H3('На каком этаже:', style={'font-family': 'Arial', 'text-align': 'center'}),
        dcc.Input(
            placeholder='На каком этаже',
            type='number',
            value=1,
            style={'width': '200px', 'margin-left': '660px'},
            min=1,
            max=40,
            required=True
        ),
        html.H3('Из скольких этажей:', style={'font-family': 'Arial', 'text-align': 'center'}),
        dcc.Input(
            placeholder='Из скольких этажей',
            type='number',
            value=5,
            style={'width': '200px', 'margin-left': '660px'},
            min=2,
            max=40,
            required=True
        ),
        html.H3('Год постройки:', style={'font-family': 'Arial', 'text-align': 'center'}),
        dcc.Input(
            placeholder='Год постройки',
            type='number',
            value=1990,
            style={'width': '200px', 'margin-left': '660px'},
            min=1960,
            max=2020,
            required=True
        ),
        html.H3('Кол-во комнат:', style={'font-family': 'Arial', 'text-align': 'center'}),
        dcc.Input(
            placeholder='Кол-во комнат',
            type='number',
            value=1,
            style={'width': '200px', 'margin-left': '660px'},
            min=1,
            max=10,
            required=True
        ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)

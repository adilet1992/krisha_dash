import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from sklearn.externals import joblib
import numpy as np

districts = ['Алатауский', 'Алмалинский', 'Ауэзовский', 'Бостандыкский', 'Жетысуский', 'Медеуский', 'Наурызбайский', 'Турксибский']
materials = ['кирпичный', 'монолитный', 'панельный']
model = joblib.load('model.pkl')

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div(
    children=[
        html.H1('Узнайте цену квартир в Алматы', style={'font-family': 'Arial', 'text-align': 'center', 'margin-bottom': '50px'}),
        html.H3('Выберите район:', style={'font-family': 'Arial', 'text-align': 'center'}),
        dcc.Dropdown(
            options=[{'label': district, 'value': district} for district in districts],
            multi=False,
            value=districts[0],
            style={'width': '300px', 'font-family': 'Arial', 'margin': 'auto'},
            clearable=False,
            id='dropdown-district'
        ),
        html.H3('Выберите тип постройки:', style={'font-family': 'Arial', 'text-align': 'center'}),
        dcc.Dropdown(
            options=[{'label': material, 'value': material} for material in materials],
            multi=False,
            value=materials[0],
            style={'width': '300px', 'margin': 'auto', 'font-family': 'Arial'},
            clearable=False,
            id='dropdown-material'
        ),
        html.H3('Площадь квартиры:', style={'font-family': 'Arial', 'text-align': 'center'}),
        dcc.Input(
            placeholder='Площадь квартиры',
            type='number',
            value=40,
            style={'width': '200px', 'margin-left': '660px'},
            min=15,
            max=500,
            required=True,
            id='input-area'
        ),
        html.H3('На каком этаже:', style={'font-family': 'Arial', 'text-align': 'center'}),
        dcc.Input(
            placeholder='На каком этаже',
            type='number',
            value=1,
            style={'width': '200px', 'margin-left': '660px'},
            min=1,
            max=40,
            required=True,
            id='input-current-floor'
        ),
        html.H3('Из скольких этажей:', style={'font-family': 'Arial', 'text-align': 'center'}),
        dcc.Input(
            placeholder='Из скольких этажей',
            type='number',
            value=5,
            style={'width': '200px', 'margin-left': '660px'},
            min=2,
            max=40,
            required=True,
            id='input-max-floor'
        ),
        html.H3('Год постройки:', style={'font-family': 'Arial', 'text-align': 'center'}),
        dcc.Input(
            placeholder='Год постройки',
            type='number',
            value=1990,
            style={'width': '200px', 'margin-left': '660px'},
            min=1960,
            max=2020,
            required=True,
            id='input-year'
        ),
        html.H3('Кол-во комнат:', style={'font-family': 'Arial', 'text-align': 'center'}),
        dcc.Input(
            placeholder='Кол-во комнат',
            type='number',
            value=1,
            style={'width': '200px', 'margin-left': '660px'},
            min=1,
            max=10,
            required=True,
            id='input-rooms'
        ),
        html.Div([
        ], id='output-price')
    ]
)

@app.callback(Output('output-price', 'children'), [Input('dropdown-district', 'value'), Input('dropdown-material', 'value'),
                                                  Input('input-area', 'value'), Input('input-current-floor', 'value'),
                                                  Input('input-max-floor', 'value'), Input('input-year', 'value'),
                                                  Input('input-rooms', 'value')])
def predict_price(district, material, area, curr_floor, max_floor, year, rooms):
    floor_coef = (curr_floor - 1) / (max_floor - 1)
    avg_sq_room = area / rooms
    oldness = 2020 - year
    params = [area, curr_floor, max_floor, rooms, year, floor_coef, avg_sq_room, oldness]
    if district == 'Алатауский':
        arr_district = [1, 0, 0, 0, 0, 0, 0, 0]
    if district == 'Алмалинский':
        arr_district = [0, 1, 0, 0, 0, 0, 0, 0]
    if district == 'Ауэзовский':
        arr_district = [0, 0, 1, 0, 0, 0, 0, 0]
    if district == 'Бостандыкский':
        arr_district = [0, 0, 0, 1, 0, 0, 0, 0]
    if district == 'Жетысуский':
        arr_district = [0, 0, 0, 0, 1, 0, 0, 0]
    if district == 'Медеуский':
        arr_district = [0, 0, 0, 0, 0, 1, 0, 0]
    if district == 'Наурызбайский':
        arr_district = [0, 0, 0, 0, 0, 0, 1, 0]
    if district == 'Турксибский':
        arr_district = [0, 0, 0, 0, 0, 0, 0, 1]
    if material == 'кирпичный':
        arr_material = [1, 0, 0]
    if material == 'монолитный':
        arr_material = [0, 1, 0]
    if material == 'панельный':
        arr_material = [0, 0, 1]
    all_params = params + arr_district + arr_material
    price = model.predict(np.array(all_params).reshape(1, -1))
    price = int(price[0])
    price = int(price/1000)*1000
    return html.H3('Цена квартиры: ' + '{:3,}'.format(price).replace(',', ' '), style={'font-family': 'Arial', 'text-align': 'center'})

if __name__ == '__main__':
    app.run_server(debug=True)

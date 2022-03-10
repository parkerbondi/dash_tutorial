# from dash import Dash, dcc, html, Input, Output
# import plotly.express as px
# import pandas as pd

# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })
# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


# app = Dash(__name__)
# app.layout = html.Div([
#     html.H1("Change the value in the text box to see callbacks in action!"),
#     html.Div([
#         "Input: ",
#         dcc.Input(id='my-input', value='asdf value', type='text')
#     ]),
#     html.Br(),
#     html.Div(id='my-output'),
#     html.H2("Another Header is placed here"),
#     dcc.Graph(id='example-graph',figure=fig)

# ])


# @app.callback(
#     Output(component_id='my-output', component_property='children'),
#     Input(component_id='my-input', component_property='value')
# )
# def update_output_div(input_value):
#     return f'Output: {input_value}'


# if __name__ == '__main__':
#     app.run_server(debug=True)
#############################################################################
# # # -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 11:24:54 2022
@author: Parker
"""
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

signal = [1,6,2,5,6,7,3,4]

# fig = px.scatter(y=signal)

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Type the next value in the box"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value=0, type='number', debounce=True)
        ]),
    dcc.Interval(id='update-interval',interval=1000,n_intervals=0),
    html.Div([
        dcc.Slider(min=0, max=20, step=1, marks={str(x):str(x)+'mm' for x in range(0,21,1)}, value=10, id='my-slider')
        ],style={'marginTop':250}),
    html.H1("The value is added to the graph below"),
    html.Div([
        dcc.Graph(id='signal-graph')
        ])
    ])


@app.callback(
    Output(component_id='signal-graph', component_property='figure'),
    Input(component_id='my-input', component_property='value'),
    Input(component_id='my-slider', component_property='value'),
    )
def update_graph(input_num,slider_num):
    signal.append(input_num+slider_num)
    fig=px.scatter(y=signal)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
#############################################################################


# from dash import Dash, dcc, html, Input, Output
# import plotly.express as px

# import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

# app = Dash(__name__)

# app.layout = html.Div([
#     dcc.Graph(id='graph-with-slider'),
#     dcc.Slider(
#         df['year'].min(),
#         df['year'].max(),
#         step=None,
#         value=df['year'].min(),
#         marks={str(year): str(year) for year in df['year'].unique()},
#         id='year-slider'
#     )
# ])


# @app.callback(
#     Output('graph-with-slider', 'figure'),
#     Input('year-slider', 'value'))
# def update_figure(selected_year):
#     filtered_df = df[df.year == selected_year]

#     fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
#                      size="pop", color="continent", hover_name="country",
#                      log_x=True, size_max=55)

#     fig.update_layout(transition_duration=500)

#     return fig


# if __name__ == '__main__':
#     app.run_server(debug=True)

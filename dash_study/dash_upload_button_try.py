# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 17:40:28 2019

@author: babin
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 16:36:26 2019

@author: babin
"""
#############################
# the simplest dash pattern
# open terminal, navigate to the project folder and run : python hello_dash_1.py
# copy host address and paste it as your browser URL
#############################



import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()

colors = {'background': 'white',
          'text': 'black',
          'graph_background': 'lightgreen',
          'paper_background': 'lightgrey'}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1(
                children="simplest dash pattern",
                style={
                        'textAlign': 'center',
                       'backroundColor': colors['text']
                       }
                ),
        
        html.Div(
                children='the example of the bar plot', 
                style={
                        'textAlign': 'center',
                        'backgroundColor': colors['background']
                        }
                ),
        
        dcc.Graph(
                id='Graph1',
                figure={
                        'data':[
                                {'x': [1, 2, 3], 'y': [5, 6, 7], 'type': 'bar', 'name': 'data_1'},
                                {'x': [1, 2, 3], 'y': [10, 11, 12], 'type': 'bar', 'name': 'data_2'}
                                ],
                        'layout':{
                                'plot_bgcolor': colors['graph_background'],
                                'paper_bgcolor': colors['paper_background'],
                                'font': {
                                        'color': colors['text']
                                        }
                                }
                        }
                    ),
        
        dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '25%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '2px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
            }
        )
    ]
)
        
        
if __name__ == '__main__':
    app.run_server(debug=True)
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 17:49:42 2019

@author: babin
"""


import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
        html.H1(children="Dash pattern"),
        html.H2(children="this simple examples demonstrates dash web interface"),
        
        
        dcc.Graph(
                id="example-graph",
                figure={
                        "data":[
                                {'x': [1, 2, 3], 'y': [4, 1, 2], 
                                 'type': 'bar', 'name': 'bar char example'},
                                {'x': [1, 2, 3], 'y': [10, 15, 5]},
                                ],
                        
                        
                        "layout":{
                                "title": "Dash example plot"
                                }
                        
                        
                        }
                )
        
        
        ]


)


if __name__ == '__main__':
    app.run_server(debug=True)
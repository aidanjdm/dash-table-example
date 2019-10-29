import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_table
import pandas as pd

########### Define your variables ######
myheading = "Best Craft Beers in DC"
mysubheading = "August 2019"
tabtitle = 'breweries'
filename = 'dc-breweries.csv'
sourceurl = 'https://www.beeradvocate.com/beer/top-rated/us/dc/'
githublink = 'https://github.com/aidanjdm/dash-table-example'

########### Set up the data
df = pd.read_csv(filename)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

##### Define the chart
trace = go.Scatter(
x = df['Alcohol By Volume (ABV)'],
y = df['Ratings (Averag)'],
hovertext = df['Beer Name'],
hoverinfo = 'text+x+y',
mode = 'markers',
marker=dict(
    size=12,
    color = df['Alcohol By Volume (ABV)'], # set color equal to a third variable
    colorscale="Blues",
    opacity=0.8,
    reversescale=False,
    showscale=True
    )
)

data = [trace]
layout = go.Layout(
    title = 'ABV vs. Average Rating', # Graph title
    xaxis = dict(title = 'ABV'), # x-axis label
    yaxis = dict(title = 'Average Rating'), # y-axis label
    hovermode ='closest' # handles multiple points landing on the same vertical
    )
fig = go.Figure(data=data, layout=layout)

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    html.H3(mysubheading),

    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    ),
    html.Br(),
    dcc.Graph(
        id='figure-1',
        figure=fig),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl)
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()

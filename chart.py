import plotly.graph_objects as go
import pandas
from datetime import datetime

df = pandas.read_csv('aapl.csv')

candlestick = go.Candlestick(x=df['date'], 
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])

fig = go.Figure(data=[candlestick])

# ignore weekends
fig.layout.xaxis.type = 'category'

shapes = [
    dict(x0='2019-01-02', x1='2019-01-02', y0=0, y1=1, xref='x', yref='paper'),
    dict(x0='2019-05-05', x1='2019-05-05', y0=0, y1=1, xref='x', yref='paper'),
    dict(x0='2019-07-30', x1='2019-07-30', y0=0, y1=1, xref='x', yref='paper'),
    dict(x0='2019-10-30', x1='2019-10-30', y0=0, y1=1, xref='x', yref='paper'),
]

annotations=[
    dict(x='2019-01-03', y=0.01, xref='x', yref='paper', showarrow=False, xanchor='left', text='Apple Cuts Guidance'),
    dict(x='2019-05-05', y=0.5, xref='x', yref='paper', showarrow=False, xanchor='left', text='Trump Tariff Tweet'),
    dict(x='2019-07-30', y=0.3, xref='x', yref='paper', showarrow=False, xanchor='left', text='Trump Tweets "China is doing very badly"'),
    dict(x='2019-10-30', y=0.3, xref='x', yref='paper', showarrow=False, xanchor='left', text='Apple Q4 Earnings'),
]

fig.update_layout(title='AAPL', annotations=annotations, shapes=shapes)

fig.show()

fig.write_html('aapl.html', auto_open=False)

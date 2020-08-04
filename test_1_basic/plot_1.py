import plotly
import plotly.graph_objs as go
import math
import numpy as np
plotly.offline.init_notebook_mode(connected=True)
trace0 = go.Bar(
    x = ['giraffes', 'orangutans', 'monkeys', 'tigers', 'rabbits'],
    y = [20, 14, 23, 5, 16],
    name = 'SF Zoo',
    # 显示为横向的Bar，但此时要改变x、y的顺序
    # orientation = 'h',
    # 直接在图上显示text的内容
    textposition = 'auto',
    # Text的内容Hover Text
    text = ["gi: 20", "or: 14", "mo: 23", "ti: 5", "ra: 16"],
    marker = dict(
        opacity=0.6,
        color='rgb(158,202,225)',
        line=dict(color='rgb(8,48,107)', width=1.5),
    )
)
trace1 = go.Bar(
    x = ['giraffes', 'orangutans', 'monkeys', 'tigers', 'rabbits'],
    y = [12, 18, 29, 8, 21],
    name = 'LA Zoo',
    # 显示为横向的Bar，但此时要改变x、y的顺序
    # orientation = 'h',
)

data = [trace0, trace1]
layout = go.Layout(
    title='SF and LA Zoo Bar',
    xaxis=dict(
        # 旋转X坐标角度
        tickangle=-45,
        tickfont=dict(size=14, color='rgb(107, 107, 107)')
    ),
    yaxis=dict(
        title='number',
        titlefont=dict(size=16, color='rgb(107, 107, 107)'),
        tickfont=dict(size=14, color='rgb(107, 107, 107)')
    ),
    legend=dict(
        # X/Y值标定图例的位置，范围从0到1
        x=0,
        y=1,
        bgcolor='rgba(0, 0, 255, 0)',
        bordercolor='rgba(0, 0, 255, 0)'
    ),
    # stack就是上下罗列
    barmode='group',
    bargap=0.15,
    bargroupgap=0.05
)
fig = go.Figure(data=data, layout=layout)
plotly.offline.iplot(fig, filename='grouped-bar')
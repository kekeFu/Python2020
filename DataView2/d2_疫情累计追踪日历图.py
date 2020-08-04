import random
import datetime

import pyecharts.options as opts
from pyecharts.charts import Calendar

from a_module1 import handle_time_list
import xlrd

"""
条形图p1
"""

file = r'D:\Users\ASUS\Documents\计算机设计大赛\数据\疫情人数.xlsx'
data = xlrd.open_workbook(file)
table = data.sheets()[1]

date = table.col_values(0)
confirm = table.col_values(1)
dead = table.col_values(2)
cure = table.col_values(3)
track = table.col_values(4)
overseas = table.col_values(5)

x1 = handle_time_list(date[1:])
y4 = track[1:]

data = []
for idx in range(len(x1)):
  data.append([x1[idx], y4[idx]])



(
    Calendar(init_opts=opts.InitOpts(width="375px", height="500px"))
    .add(
        series_name="",
        yaxis_data=data,
        calendar_opts=opts.CalendarOpts(
            pos_top="120",
            pos_left="30",
            pos_right="30",
            range_=["2020-01-11", "2020-05-31"],
            yearlabel_opts=opts.CalendarYearLabelOpts(is_show=False),
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(pos_top="30", pos_left="center", title="2020年疫情新增追踪情况"),
        visualmap_opts=opts.VisualMapOpts(
            max_=3147, min_=0, orient="horizontal", is_piecewise=False, pos_bottom="160",
        ),
    )
    .render("s2_新增追踪日历图.html")
)

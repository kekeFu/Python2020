import pyecharts.options as opts
from pyecharts.charts import Bar, Line
from a_module1 import handle_time_list
import xlrd

"""
 疫情态势
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

x_data = handle_time_list(date[1:])
y1 = confirm[1:]
y2 = dead[1:]
y3 = cure[1:]
y4 = track[1:]
y5 = overseas[1:]

bar = (
    Bar(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="蒸发量",
        yaxis_data=y1,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="降水量",
        yaxis_data=y2,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="温度",
            type_="value",
            min_=0,
            max_=25,
            interval=5,
            axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
        )
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(
            is_show=True, trigger="axis", axis_pointer_type="cross"
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
        ),
        yaxis_opts=opts.AxisOpts(
            name="水量",
            type_="value",
            min_=0,
            max_=250,
            interval=50,
            axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
)

line = (
    Line()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="平均温度",
        yaxis_index=1,
        y_axis=[2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
        label_opts=opts.LabelOpts(is_show=False),
    )
)

bar.overlap(line).render("mixed_bar_and_line.html")

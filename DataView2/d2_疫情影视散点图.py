from pyecharts import options as opts
from pyecharts.charts import Grid, Scatter

from a_module1 import handle_time_list
import xlrd

"""
 疫情态势
"""

file = r'D:\Users\ASUS\Documents\计算机设计大赛\数据\疫情-影视.xlsx'
data = xlrd.open_workbook(file)
table = data.sheets()[1]

date = table.col_values(0)
confirm = table.col_values(1)
tickets = table.col_values(2)

x1 = handle_time_list(date[1:])
y1 = tickets[1:]
y2 = confirm[1:]

scatter = (
    Scatter(init_opts=opts.InitOpts(width="375px", height="500px",))
    .add_xaxis(x1)
    .add_yaxis("票房", y1, yaxis_index=0, color="#d14a61",
               label_opts=opts.LabelOpts(is_show=False),)
    .add_yaxis("确诊", y2, yaxis_index=1, color="#5793f3",
               label_opts=opts.LabelOpts(is_show=False),)
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="新增票房",
            type_="value",
            min_=-3910,
            max_=8050,
            position="left",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#5793f3")
            ),
            # axislabel_opts=opts.LabelOpts(formatter="{value} 万"),
        )
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            type_="value",
            name="新增确诊",
            min_=0,
            max_=15200,
            position="right",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#d14a61")
            ),
            # axislabel_opts=opts.LabelOpts(formatter="{value} 人"),
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
            ),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="每日票房和确诊人数变化", pos_top="1%"),
        visualmap_opts=opts.VisualMapOpts(type_="size", max_=2, min_=1),
        datazoom_opts=[opts.DataZoomOpts()],
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_left="60%"),
    )
    .render("s4_疫情影视散点图.html")
)

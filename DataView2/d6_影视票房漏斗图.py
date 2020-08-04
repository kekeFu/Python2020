import pyecharts.options as opts
from pyecharts.charts import Funnel

from a_module1 import handle_time_list
import xlrd


"""
    影视累积票房
"""

file = r'D:\Users\ASUS\Documents\计算机设计大赛\数据\2019.1.11-2019.5.31影视排序数据.xlsx'
data = xlrd.open_workbook(file)
table = data.sheets()[1]


Name = table.col_values(0)
counts = table.col_values(1)

x_data = Name[1:]
y_data = counts[1:]

data = [[x_data[i], y_data[i]] for i in range(len(x_data))]

(
    Funnel(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(
        series_name="",
        data_pair=data,
        gap=2,
        tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%"),
        label_opts=opts.LabelOpts(is_show=True, position="inside"),
        itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="上榜次数排名前10", subtitle="网络电影票房数"))
    .render("s6_网络电影票房数上榜次数排名前10.html")
)

from pyecharts import options as opts
from pyecharts.charts import Pie
from a_module1 import handle_time_list
import xlrd


# 读取数据
file = r'D:\Users\ASUS\Documents\计算机设计大赛\数据\2019.1.11-2019.5.31影视排序数据.xlsx'
data = xlrd.open_workbook(file)
table = data.sheets()[1]

name = table.col_values(0)
count = table.col_values(1)


x1 = name[1:10]
y2 = count[1:10]

v = x1
c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(v, y2)],
        radius=["30%", "75%"],
        center=["50%", "50%"],
        rosetype="area",
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="电影上榜次数top10"),
                     legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"),
                     )
    .render("s3_电影上榜次数前10饼图.html")
)

from pyecharts import options as opts
from pyecharts.charts import Bar

c = (
    Bar()
    .add_dataset(
        source=[
            ["score", "amount", "product"],
            [89.3, 58212, "Matcha Latte"],
            [57.1, 78254, "Milk Tea"],
            [74.4, 41032, "Cheese Cocoa"],
            [50.1, 12755, "Cheese Brownie"],
            [89.7, 20145, "Matcha Cocoa"],
            [68.1, 79146, "Tea"],
            [19.6, 91852, "Orange Juice"],
            [10.6, 101852, "Lemon Juice"],
            [32.7, 20112, "Walnut Brownie"],
        ]
    )
    .add_yaxis(
        series_name="",
        yaxis_data=[],
        encode={"x": "amount", "y": "product"},
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Dataset normal bar example"),
        xaxis_opts=opts.AxisOpts(name="amount"),
        yaxis_opts=opts.AxisOpts(type_="category"),
        visualmap_opts=opts.VisualMapOpts(
            orient="horizontal",
            pos_left="center",
            min_=10,
            max_=100,
            range_text=["High Score", "Low Score"],
            dimension=0,
            range_color=["#D7DA8B", "#E15457"],
        ),
    )
    .render("dataset_bar_1.html")
)

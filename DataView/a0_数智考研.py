import json
import pandas as pd
import numpy as np
import jieba
import jieba.analyse
from pyecharts import options as opts
from pyecharts.charts import Geo, Map, Bar, Line, Page, Pie, Boxplot, Funnel
from pyecharts.globals import ChartType, SymbolType,ThemeType


# 2019-2020全国各省市考研报考人数分布
def setmap():
    area = ['北京', '江苏', '湖北', '河北', '辽宁', '四川', '山东', '湖南', '甘肃', '内蒙古', '海南', '云南', '广东', '广西', '陕西', '黑龙江', '河南',
            '吉林', '重庆', '上海', '浙江', '宁夏', '江西', '安徽', '山西', '天津', '福建', '新疆', '贵州', '西藏', '青海']
    year19 = [38.3, 21.2, 14.4086, 14.7188, 10.9567, 14.1786, 25.4486, '——', 5.5345, 5.9569, '——', 4.9496, 14.0, 4.3,
              '——', 9.0466, 23.36, '——', '——', '——', '——', '——', 7.8531, '——', '——', 5.7956, 5.8, 3.6022, '——', 0.3641,
              0.8829]
    year20 = [42.5, 24.9, 16.28, '——', 11.9081, 17.4815, 31.319, 12.2847, 6.23, 7.5366, '——', '——', 17.4, 5.38, '——',
              9.9126, '——', 8.0852, 7.9248, '——', 11.0, '——', 9.6505, 16.5, '——', 6.8458, '——', 4.2597, 5.8589, '——',
              '——']
    area_y19 = [list(z) for z in zip(area, year19)]
    area_y20 = [list(z) for z in zip(area, year20)]

    c = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS))
            .add("2019年", area_y19, "china",
                 is_map_symbol_show=False, label_opts=opts.LabelOpts(color="#fff"),
                 tooltip_opts=opts.TooltipOpts(is_show=True), zoom=1.2, center=[105, 30])
            .add("2020年", area_y20, "china",
                 is_map_symbol_show=False, label_opts=opts.LabelOpts(color="#fff"),
                 tooltip_opts=opts.TooltipOpts(is_show=True), zoom=1.2, center=[105, 30])
            .set_series_opts(label_opts=opts.LabelOpts())  # is_show=False
            .set_global_opts(title_opts=opts.TitleOpts(title="各省市考研报考人数分布", pos_top='5%',
                                                       title_textstyle_opts=opts.TextStyleOpts(color="#FF0000")),
                             visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pos_right=0, pos_bottom=0,
                                                               textstyle_opts=opts.TextStyleOpts(color="#F5FFFA"),
                                                               pieces=[
                                                                   {"min": 15, "label": '>15 万', "color": "#893448"},
                                                                   {"min": 10, "max": 15, "label": '10-15 万',
                                                                    "color": "#ff585e"},
                                                                   {"min": 5, "max": 10, "label": '5-10 万',
                                                                    "color": "#fb8146"},
                                                                   {"min": 1, "max": 5, "label": '1-5 万',
                                                                    "color": "#ffb248"},
                                                                   {"min": 0, "max": 1, "label": '0-1 万',
                                                                    "color": "#fff2d1"}])))

    return c


# 近5年理学/文学国家线趋势
def setrose():
    x1 = ['2016年', '2017年', '2018年', '2019年', '2020年']
    y1 = ['文学', 350.0, 345.0, 345.0, 355.0, 355.0]
    y2 = ['理学', 285.0, 290.0, 280.0, 290.0, 288.0]

    c = (
        Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
            .add_xaxis(xaxis_data=x1)
            .add_yaxis(
                series_name="文学",
                y_axis=y1,
                markpoint_opts=opts.MarkPointOpts(
                    data=[
                        opts.MarkPointItem(type_="max", name="最大值"),
                        opts.MarkPointItem(type_="min", name="最小值"),
                    ]
                ),
                markline_opts=opts.MarkLineOpts(
                    data=[opts.MarkLineItem(type_="average", name="平均值")]
                ),
            )
            .add_yaxis(
                series_name="理学",
                y_axis=y2,
                markpoint_opts=opts.MarkPointOpts(
                    data=[opts.MarkPointItem(type_="max", name="最大值"),
                          opts.MarkPointItem(type_="min", name="最小值"),
                          ]
                ),
                markline_opts=opts.MarkLineOpts(
                    data=[
                        opts.MarkLineItem(type_="average", name="平均值"),
                        opts.MarkLineItem(symbol="none", x="90%", y="max"),
                        opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
                    ]
                ),
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="近5年理学/文学国家线趋势"),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                toolbox_opts=opts.ToolboxOpts(is_show=True),
                xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
            )
    )

    return c


# 理学/哲学/历史学国家线对比
def setbar():
    x1 = ['2016年', '2017年', '2018年', '2019年', '2020年']
    y1 = [285.0, 290.0, 280.0, 290.0, 288.0]    # 理学
    y2 = [280.0, 285.0, 280.0, 295.0, 300.0]    # 哲学
    y3 = [315.0, 315.0, 315.0, 325.0, 324.0]    # 历史学
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))  # 设置主题
            .add_xaxis(x1)
            .add_yaxis('理学', y1)
            .add_yaxis('哲学', y2)
            .add_yaxis('历史学', y3)
            .set_global_opts(title_opts=opts.TitleOpts(title="理学/哲学/历史学国家线对比"))
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            # 插入平均值线
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average", name="平均值"), ]),
            # 插入最大值最小值点
            markpoint_opts=opts.MarkPointOpts(data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="min", name="最小值"),
            ])
        )
    )

    return c


# 报名数和录取数对比
def setpai():
    y = ['2015年', '2016年', '2017年', '2018年', '2019年', '2020年']
    r1 = [164.9, 177.0, 201.0, 238.0, 290.0, 341.0]
    r2 = [64.5055, 66.7064, 80.6103, 85.7966, 91.6503, '一 一']
    r1 = [list(z) for z in zip(y, r1)]
    r2 = [list(z) for z in zip(y, r2)]

    c = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT,  bg_color="transparent"))
            .add("", r1, center=["50%", "60%"], radius=[75, 100])
            .add("", r2, center=["50%", "60%"], radius=[0, 50])
            .set_global_opts(title_opts=opts.TitleOpts("近五年报名数和录取数对比"),legend_opts=opts.LegendOpts(type_="scroll", textstyle_opts=opts.TextStyleOpts(color="#FFFFFF")))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}")))

    return c


# 2018年报名数、招生数、录取数漏斗图
def setfunnel():
    data = [['报名人数/万', 238], ['招生人数', 85.7966], ['录取人数', 76.2]]

    c = (
        Funnel(init_opts=opts.InitOpts(width="300x", height="600px"))
        .add(
            series_name="",
            data_pair=data,
            gap=2,
            tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%"),
            label_opts=opts.LabelOpts(is_show=True, position="inside"),
            itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="2018年报名数、招生数、录取数漏斗图"))
    )
    return c


page = Page(page_title="数智考研", layout=Page.DraggablePageLayout)
page.add(setmap(), setrose(),  setbar(), setpai(), setfunnel())
# page.render("test.html")
Page.save_resize_html("test.html", cfg_file="chart_config1.json", dest="数智考研大屏可视化系统.html")




from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.globals import ThemeType


# 2019-2020全国各省市考研报考人数分布
area = ['北京', '江苏', '湖北', '河北', '辽宁', '四川', '山东', '湖南', '甘肃', '内蒙古', '海南', '云南', '广东', '广西', '陕西', '黑龙江', '河南', '吉林', '重庆', '上海', '浙江', '宁夏', '江西', '安徽', '山西', '天津', '福建', '新疆','贵州', '西藏', '青海']
year19 = [38.3, 21.2, 14.4086, 14.7188, 10.9567, 14.1786, 25.4486, '——', 5.5345, 5.9569, '——', 4.9496, 14.0, 4.3, '——', 9.0466, 23.36, '——', '——', '——', '——', '——', 7.8531, '——', '——', 5.7956, 5.8, 3.6022, '——', 0.3641, 0.8829]
year20 = [42.5, 24.9, 16.28, '——', 11.9081, 17.4815, 31.319, 12.2847, 6.23, 7.5366, '——', '——', 17.4, 5.38, '——', 9.9126, '——', 8.0852, 7.9248, '——', 11.0, '——', 9.6505, 16.5, '——', 6.8458, '——', 4.2597, 5.8589, '——', '——']

area_y19 = [list(z) for z in zip(area, year19)]
area_y20 = [list(z) for z in zip(area, year20)]

area_map = (
    Map(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS))
        .add("2019年", area_y19, "china",
             is_map_symbol_show=False, label_opts=opts.LabelOpts(color="#fff"),
             tooltip_opts=opts.TooltipOpts(is_show=True), zoom=1.2, center=[105, 30])
        .add("2020年", area_y20, "china",
             is_map_symbol_show=False, label_opts=opts.LabelOpts(color="#fff"),
             tooltip_opts=opts.TooltipOpts(is_show=True), zoom=1.2, center=[105, 30])
        .set_series_opts(label_opts=opts.LabelOpts())   # is_show=False
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
                                                                "color": "#fff2d1"}]))
        .render("s1_2019-2020全国各省市考研报考人数分布.html"))
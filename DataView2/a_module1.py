import xlrd


def handle_time_list(time_list):
    """
    处理float格式的时间数据为 年/月/日 小时:分钟
    time_list: 时间列表
    return: 处理好的时间数据列表
    """
    new_time_list = [xlrd.xldate_as_datetime(i, 0).strftime(r'%Y/%m/%d') for i in time_list]
    return new_time_list


if __name__ == '__main__':
    print('处理float格式的时间数据为 年/月/日 小时:分钟')
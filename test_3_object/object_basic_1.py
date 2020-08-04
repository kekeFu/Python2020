"""
面向对象：抽象化编程思想.
类，对象：用类来创建（实例化）对象.
类：一系列特征和行为相同的事物总和，
    1.属性：特征
    2.行为：方法

定义类 :
PEP 8要求标识符的名字用全小写多个单词用下划线连接
但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
一个类可创作多个对象，self 地址不同
"""


class Washer1():
    def wash(self):
        # wash()，实例化方法,
        # self, 调用该函数的对象
        # print(self)   # 对象地址
        print('洗衣服')

    def p_info(self):
        print(f'高度：{self.height}')


def main1():
    # 创建对象
    haier1 = Washer1()
    # print(haier1)   # <__main__.Washer object at 0x01490F40>
    haier1.height = 30
    print(haier1.height)
    haier1.p_info()


"""
魔法方法：__xx__(),具有特殊功能的函数
    1.__init__(self): 初始化对象属性
    2.__str__(): return 
    3.__del__(): 删除对象
"""


class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return '这是格力洗衣机的说明书'

    def __del__(self):
        print('对象已经删除')

    def p_info(self):
        print(f'宽度={self.width}, 高度={self.height}')


def test1():
    geli1 = Washer(1, 2)
    print(geli1)  # 这是格力洗衣机的说明书
    geli1.p_info()
    # del geli1
    # print(geli1)      # 此时geli1 已删除，会报错


"""" 
定义一个类描述数字时钟。 
属性：小时，分钟，秒
方法：显示当前时间，设置时间
"""


class Digital_clock(object):
    def __init__(self, year, month, day, hour, min):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.min = min
        self.week = 0

    def display_time(self):
        print(self.year, self.month)


def test2():
    o = Digital_clock(2020, 2, 12, 12, 49)
    o.display_time()


if __name__ == '__main__':
    main1()

"""
Date：2020.2.9

测试案例：烤地瓜
需求分析
1.烤的时间和对应的地瓜状态：
2.烤制过程
步骤：
    1.定义类, 地瓜属性，状态，烤的时间，调料
    2.定义方法，怎样烤制
    3.创建地瓜对象
"""


# 定义地瓜类
class SweetPotato:
    def __init__(self):
        self.cook_time = 0
        self.cook_state = '生的'
        self.condiments = []

    def cook(self, time):
        """烤地瓜方法"""
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生不熟的'
        elif 5 <= self.cook_time < 8:
            self.cook_state = '熟的'
        elif 8 <= self.cook_time:
            self.cook_state = '烤糊的'

    def add_condiments(self, condiment):
        self.condiments.append(condiment)

    def __str__(self):
        return f'这个地瓜的烤制时间：{self.cook_time}分钟，' \
               f'状态：{self.cook_state}，调料有{self.condiments}'


def main():
    digua1 = SweetPotato()
    print(digua1)
    digua1.cook(5)
    digua1.add_condiments('盐')
    print(digua1)
    digua1.add_condiments('辣椒面儿')
    print(digua1)


if __name__ == '__main__':
        main()
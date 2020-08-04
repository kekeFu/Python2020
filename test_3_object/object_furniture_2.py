"""
date:   2020.2.9
搬家具：将小于房子剩余面积的家具搬进房子
1.定义家具类，房屋类
"""


class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area


class House():
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area
        self.furniture = []

    def __str__(self):
        return f'房子地理位置在{self.address},' \
               f'房屋面积是{self.area},' \
               f'房屋剩余面积是{self.free_area},' \
               f'房屋内家具列表是{self.furniture}'

    def add_furniture(self, item):
        """容纳家具"""
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('房子面积不足！')


def main():
    bed = Furniture('架子床', 4)
    sofa = Furniture('沙发', 100)
    h1 = House('上海', 100)
    print(h1)
    h1.add_furniture(bed)
    print(h1)
    h1.add_furniture(sofa)
    print(h1)


if __name__ == '__main__':
    main()
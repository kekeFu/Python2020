"""
私有属性和私有方法
以两个__来命名,   get_xx: 获取私有属性
                 set_xx: 修改
"""


class Master(object):
    def __init__(self):
        self.kongfu = '[古法]'
        # self.__money

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼')


class School(object):
    def __init__(self):
        self.kongfu = '[有名法]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼')


class Prentice(School, Master):
    """重写"""
    def __init__(self):
        super().__init__()
        self.kongfu = '[独创]'
        self.__money = 20

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼')

    def __info_print(self):
        print('这是私有方法！')

    def get_money(self):
        return self.__money

    def set_money(self):
        self.__money = 2020


class Tusun(Prentice):
    pass


def main1():
    da = Tusun()
    print(da.get_money())
    da.set_money()
    print(da.get_money())

"""
另一种理解：
    实际上私有属性存在一个坑点，即通过换名仍然可以访问私有属性；
    命名时最好以_开头（一种规范）；
    用getter(访问器)和setter(修改器)来访问与修改属性值；
    用 @property装饰器 来包装getter和setter方法；
"""


class Master1(object):
    """验证私有方法"""
    def __init__(self):
        self.kongfu = '[古法煎饼]'
        self.__money = 10000  # 私有属性

    def __make_cake(self):
        return f'用{self.kongfu}制作煎饼果子' \
                f'花费了{self.__money}￥'


class School1:
    def __init__(self, kongfu, money):
        self._kongfu = kongfu
        self._money = money

    # 访问器 - getter方法
    @property
    def money(self):
        return self._money

    @property
    def kongfu(self):
        return self._kongfu

    # 修改器 - setter方法
    @money.setter
    def money(self, money):
        self._money = money

    def make_cake(self):
        print(f'用{self._kongfu}制作煎饼{self._money}')


def main2():
    """换名访问私有属性和方法"""
    t1 = Master1()
    print(t1._Master1__money)
    # 10000 ，运用命名的变换成功访问私有属性
    print(t1._Master1__make_cake)
    # 打印了t1地址，需有一个变量来接收


def main3():
    """修改私有量"""
    school = School1('有名法', 100)
    school.make_cake()
    school.money = 10
    school.make_cake()
    # school.kongfu = '古法'
    # AttributeError: can't set attribute


if __name__ == '__main__':
    main1()
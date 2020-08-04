"""
.多继承：默认使用第一个父类的同名属性和方法
.重写：若子类和父类有同名属性和方法，则调用子类的
"""


class Master(object):
    def __init__(self):
        self.kongfu = '[古法]'

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

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼')


def main():
    da = Prentice()
    print(da.kongfu)
    da.make_cake()


if __name__ == '__main__':
    main()

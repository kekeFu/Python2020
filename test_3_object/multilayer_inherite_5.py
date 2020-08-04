"""
多层继承：Multilayer inheritance
__mro__: 查看继承关系
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
        """ 若不初始化，则上一次self的值会保留下来"""
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼')

    def master_cake(self):
        """
        再次封装
        再次调用初始化
        """
        Master.__init__(self)
        Master.make_cake(self)

    def school_cake(self):
        School.__init__(self)
        School.make_cake(self)


class Tusun(Prentice):
    pass


def main():
    t = Tusun()
    t.make_cake()
    t.master_cake()

    print(Tusun.__mro__)
    # __mro__: 查看继承关系
    # (<class '__main__.Tusun'>, <class '__main__.Prentice'>,
    # <class '__main__.School'>, <class '__main__.Master'>,
    # <class 'object'>)


if __name__ == '__main__':
    main()
"""
子类调用父类的同名属性和同名方法
Child class calls the same name attribute
and method of the parent class.
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


def main():
    da = Prentice()
    da.make_cake()
    da.master_cake()
    # da.make_cake()


if __name__ == '__main__':
    main()

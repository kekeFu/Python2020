"""
.super：子类重写了父类方法，并在重写方法中调用父类方法
        super(当前类，self).当前方法
"""


class Master(object):
    def __init__(self):
        self.kongfu = '[古法]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼')


class School(Master):
    def __init__(self):
        super().__init__()
        self.kongfu = '[有名法]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼')

        # 2.1 supper() 带参数法
        super(School, self).__init__()
        super(School, self).make_cake()

        # 2.2 super() 无参数
        # super().__init__()
        # super().make_cake()


class Prentice(School):
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

    def old_cake(self):
        # 法1
        # Master.__init__(self)
        # Master.make_cake(self)
        # School.__init__(self)
        # School.make_cake(self)

        # 法2：supper（）带参数
        super(Prentice, self).__init__()
        super(Prentice, self).make_cake()

        # 法3：supper() 无参数
        # super().__init__()
        # super().make_cake()


def main():
    da = Prentice()
    da.make_cake()
    da.old_cake()
    da.make_cake()


if __name__ == '__main__':
    main()
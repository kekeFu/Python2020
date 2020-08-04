"""
class 类名（object<父类>）
继承：子类继承父类
.单继承；
"""


class A(object):
    """单继承, 父类"""
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)


class B(A):
    """子类"""
    pass


def main():
    """单继承示例"""
    r = B()
    r.info_print()      # 1


if __name__ == '__main__':
    main()
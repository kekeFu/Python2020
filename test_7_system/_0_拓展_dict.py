class A(object):
    a = 0

    def __init__(self):
        self.b = 1


def t1():
    """测试"""
    aa = A()
    print(A.__dict__)
    print(aa.__dict__)


if __name__ == '__main__':
    t1()

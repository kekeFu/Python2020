"""
制作模块
每个 python 文件都可作为一个模块，模块名就是文件名字。
自定义模块必须满足标识符命名规则.。
"""
import math


def t_1(a, b):
    print(math.fabs(a+b))


def t_2(a, b):
    print(a * b)


# print(__name__)     # __main__
if __name__ == '__main__':
    """
    测试信息
    __name__:系统变量，模块标识符，
    值，需根据使用位置来确定
    在自身文件中：__main__
    在其他文件中：模块名字
    main:
    """
    t_1(1, 2)
    t_2(2, 3)

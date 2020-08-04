"""
模块（）：
一个python文件，以 .py 结尾，包含python对象定义和语句。
模块可以定义函数、类、变量，也可包含可执行文件

导入模块：
        1.import  模块名
        2.from 模块名 import 功能名
"""
from random import *

print(sqrt(9))


def t1():
    import random
    print(random.sqrt(9))     # 3.0, 浮点数


def t2():
    from random import sqrt, fabs
    print(sqrt(9), fabs(9))


# def t3():
#     from math import *
#     """
#     SyntaxError:
#     import * only allowed at module level
#     """
#     print(sqrt(9))

def t4():
    """定义别名
    import 模块名 as 别名
    from 模块名 import 功能名 as 别名
    """
    import time as tt
    tt.sleep(2)
    # time.sleep(2)     # 使用别名后，原来的名字被替代
    # NameError: name 'time' is not defined
    print('hello')

    # from time import sleep as s1
    # s1(2)
    # print('hello')


def t5():
    pass


if __name__ == '__main__':
    t1()
    t2()
    t4()
    t5()


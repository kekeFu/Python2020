import math

__all__ = ['t_1']
# 若有其他文件调用本文件，则只导入t_1()


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

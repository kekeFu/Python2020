"""
包：有联系的模块组织在一起，放到同一个文件夹，
    并自动创建一个__init__.py文件
制作包：new ——> 包名 ——> Enter ——> 制作模块
导入包：
    1.import 包名
    2.from 包名 import *
"""
import my_module1


def t1():
    import mypakage.my_module1
    mypakage.my_module1.info_print()


def t2():
    """
    必须先在 __init__.py 文件中添加 __all__ = []
    控制允许导入的模块
    原因：不同模块内可能有相同名字的功能
    """
    pass


from mypakage import *
my_module1.info_print()


# if __name__ == '__main__':
#     # t1()
#     t2()

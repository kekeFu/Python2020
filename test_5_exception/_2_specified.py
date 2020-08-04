"""
1.捕获指定异常，异常类型有多种
2.若尝试执行的代码异常类型与捕获的异常类型不同则报错
3.try下方一般只放一行代码，若有多行可能异常代码，
则捕获一个异常类型后函数返回，及只能捕获一个异常类型。
4.捕获多个指定异常
5.捕获所有异常，Exception 是所有程序异常类的父类
"""


# 异常类型：NameError
# print(n)

# 异常类型：ZeroDivisionError
# print(1/0)


def t1():
    try:
        print(num)
    except NameError:
        print('有错误')


def t2():
    try:
        print('you')
        print(num)
        print(1/0)
    except ZeroDivisionError:
        print('有错误')


def t3():
    """
    捕获多个指定异常
    捕获异常描述信息
    """
    try:
        print(num)
    except (NameError, ZeroDivisionError) as result:
        print(result)
        # name 'num' is not defined


def t4():
    try:
        print(num)
    except Exception as result:
        print(result)


if __name__ == '__main__':
    # t1()
    # t2()
    # t3()
    t4()

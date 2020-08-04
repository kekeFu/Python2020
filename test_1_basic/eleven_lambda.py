"""
lambda 参数列表 : 返回值
lambda 参数形式：
    1.无参数：lambda：100
    2.一个参数：lambda a: a
    3.默认参数：lambda a, b, c=100: a + b + c
    4.可变参数：*args,返回元组
    lambda *args: args
    5.可变参数：*kwargs,返回字典
    lambda **kwargs: kwargs

lambda 应用：简化代码
    1.判断，lambda a, b: a if a > b else b
    2.列表数据按字典 key 值排序
"""


# def fn1():
#     return 100


# def de1():
#     r = fn1()
#     print(r)
#     r2 = lambda: 100
#     print(r2)           # 地址：<function main.<locals>.<lambda> at 0x00CCD6E8>
#     print(r2())         # 返回值：100


# def test2():
"""
lambda 测试案例
"""
#     fn1 = lambda a, b: a + b
#     print(fn1(1, 2))
#     fn2 = lambda *args: args
#     print(fn2(1, 2, 3))
#     print(fn2(1, 3))
#     print(fn2(1))       #  (1,)
#     fn3 = lambda **kwargs: kwargs
#     print(fn3(name='py', age=30))
#
#     fn4 = lambda a, b: a if a > b else b
#     print(fn4(100, 200))
#
#     student = [{'name': 'a', 'id': '1', 'tel': 'a1'},
#         {'name': 'b', 'id': '2', 'tel': 'b2'},
#         {'name': 'c', 'id': '3', 'tel': 'c3'}]
#     student.sort(key=lambda x: x['name'])
#     print(student)
#     student.sort(key=lambda x: x['name'], reverse=True)
#     print(student)
#     student.sort(key=lambda x: x['id'])
#     print(student)


"""
高阶函数：def add_num(a, b, f)
内置高阶函数：
    1.map(func, list)：
    将func 应用于list中的每一个元素，返回一个迭代器
    2.reduce(func, list)：
    计算结果与下一个数据做累积计算，必须有两个参数
    from functools import reduce
    3.filter(func, list)：
    过滤掉不符合条件的元素，返回一个filter对象，可用list()转换
"""

# def add_num(a, b, f):
#     # 传入函数 f
#     return f(a) + f(b)


# def func(x):
#     return x ** 2

from functools import reduce


def add_2(a, b):
    return a + b


def func3(x):
    return x % 2 == 0


def main():
    """
    体验高阶函数
    :return:
    """
    # print(abs(-2))          # 求绝对值
    # print(round(0.1))       # 四舍五入
    # s1 = add_num(1, 2, abs)
    # s2 = add_num(1, 2.5, round)
    # print(s1, s2)

    list1 = [1, 2, 3, 4, 5]
    # map(func, list1)
    # print(list(map(func, list1)))
    # s = reduce(add_2, list1)
    # print(s)
    r = filter(func3, list1)
    print(r)        # <filter object at 0x00CAE2E0>
    print(list(r))  # [2, 4]


if __name__ == '__main__':
    main()

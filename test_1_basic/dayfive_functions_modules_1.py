# def sum1(a, b):
#     """
#     求和函数sum1
#     :param a: 参数1
#     :param b: 参数2
#     :return: a + b
#     """
#     return a + b
#
#
# help(sum1)

# 打印,注意复制用法！
# def print_star(i):
#     print('*' * i)
#
#
# def fact(j):
#     for n in range(1, j + 1):
#         print_star(n)
#
#
# while True:
#     a = int(input("a = "))
#     fact(a)

#
# def ts():
#     # return 30, 1
#     # return 后面可直接书写，元组(默认)，列表，字典，即返回多个值
#     return [1, 2]
#
#
# def ta(nu):
#     print(nu)
#
#
# a = ts()
# ta(a)
# ta(ts())
#
# def use(*args):
#     print(args)
#
# # 组包
# use('name', 1)
# def use(**kwargs):
#     print(kwargs)
#
#
# use(name='ton', age=1)

# 元组拆包
# def ts():
#     return 30, 1
#
#
# n1, n2 = ts()
# print(n1)
# print(n2)
# 列表拆包
# def ts():
#     return [30, 1]
#
#
# n = ts()
# print(n[0])
# print(n[1])
# 字典拆包
# def ts():
#     return {'name': 'TOM', 'age': '12'}
#
#
# n = ts()
# n1, n2 = n
# print(n1, end=" ")
# print(n2)
# print(n[n1], end=" ")
# print(n[n2])

# 交换变量
# a, b = 1, 2
# print(f'a = {a} b = {b}')
# a, b = b, a
# print(f'a = {a} b = {b}')

# 引用
# int 类型
# a = 1
# b = a
# print(b)        # 1
# print(id(a))    # 1795942320
# print(id(b))    # 1795942320
# a = 2
# print(b)        # 1 说明 int类型 为不可变类型

# 引用
# 列表
# a = [1, 2]
# b = a
# print(b)        # [1, 2]
# print(id(a))    # 17421000
# print(id(b))    # 17421000
# a.append(30)
# print(b)        # [1, 2, 30] 说明 列表类型 为可变类型

# 引用可当做实参！
def ts(a):
    print(f'a = {a} ,id = {id(a)}')
    a += a
    print(f'a = {a} ,id = {id(a)}')


ts(10)          # id 发生变化
ts([10, 1])     # id 不变

"""
可变类型：字典，列表，集合
不可变：元组，整型，浮点型
"""
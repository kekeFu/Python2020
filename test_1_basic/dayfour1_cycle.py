"""
Function_1:  寻找水仙花数。
水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
Time:        2020.1.28
Author:      YaoXie
"""
# for i in range(100, 1000, 1):
#     a = i % 10              # 求得个位数
#     b = int(i / 100)        # 求得百位数
#     c = int(i / 10 % 10)    # 求得十位数
#     d = a ** 3 + b ** 3 + c ** 3
#     if d == i:
#         print(f'{i}是水仙花数')

"""
Function_2:  将一个正整数反转

Time:        2020.1.28
Author:      YaoXie
"""
# # METHOD1
# while True:
#     a = int(input("\n Enter a positive number: \n"))
#     while a > 0:
#         b = a % 10
#         print(f'{b}', end="")
#         a //= 10

# METHOD2: 骆昊的方法
# while True:
#     num = int(input('num = '))
#     reversed_num = 0
#     while num > 0:
#         reversed_num = reversed_num * 10 + num % 10
#         num //= 10
#     print(reversed_num)

"""
Function_3:  百钱百鸡问题。
公鸡5元一只，母鸡3元一只，小鸡1元三只，
用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
Time:        2020.1.28
Author:      YaoXie
"""
# while True:
#     num = int(input("请输入总数：\n"))
#     count = 0
#     for i in range(1, num+1):
#         for j in range(1, num + 1):
#             for k in range(1, num + 1):
#                 z = 5*i + 3*j + 1*k
#                 if z == num:
#                     print(f'公鸡：{i} 只,母鸡：{j} 只,小鸡：{k} 只')
#                     count += 1
#     print(f'{num}元时，总共有{count}种买法')

"""
总结：上面所用的方法是————穷举法，也称为暴力搜索法，
通过列举，一项一项地判断，直到找出所有符合条件的选项
"""

"""
Function_4:  生成斐波那契数列的前20个数。

特点：数列的前两个数都是1，
从第三个数开始，每个数都是它前面两个数的和，
形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。

Time:        2018-03-02
Author:      骆昊
"""
# while True:
#     fib = int(input("\n请输入要生成的个数:\n"))
#     a = 0
#     b = 1
#     count = 0
#     for _ in range(fib):
#         a, b = b, a + b     # 两数交换，即：b = a+b, a = b
#         count += 1
#         print(a, end=' ')
#         if count % 5 == 0:
#             print()

"""
Function_5:  找出10000以内的完美数。

完美数又称为完全数或完备数，
它的所有的真因子（即除了自身以外的因子）的和
（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。

Time:        2020.1.28
Author:      YaoXie
"""
# while True:
#     num = int(input('请输入数的范围：\n'))
#     for i in range(2, num+1, 1):
#         z = 0
#         for j in range(1, i, 1):
#             k = i % j
#             if k == 0:
#                 z = z + j
#         if z == i:
#             print(f'完美数：{i} ')

"""
Version: 0.1
Author: 骆昊
Date: 2018-03-02

import math

for num in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            # 敲重点！再此向罗大神膜拜！
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)
"""


"""
Function_6:  输出100以内所有的素数。

素数指的是只能被1和自身整除的正整数（不包括1）。

Time:        2020.1.28
Author:      YaoXie
"""
# from math import sqrt
#
# while True:
#     num = int(input('请输入数的范围：\n'))
#     count = 0
#     for j in range(2, num + 1):
#         is_prime = True
#         for i in range(2, int(sqrt(j)) + 1, 1):
#             k = j % i
#             if k == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             count += 1
#             print(f'{j}', end=" ")
#             if count % 5 == 0:
#                 print()
#     print(f'\n总共有{count}个素数\n')

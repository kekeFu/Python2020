"""
Function_1:  for-in循环
用for循环实现1~100之间的奇数求和

Time:        2020.1.27
Author:      YaoXie
"""
# sumup = 0
# for x in range(2, 101, 2):
#     print(x)
#     sumup += x
# print(sumup)

"""
Function_2:  while循环
输入一个正整数判断是不是素数。
质数又称素数。
一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数；
否则称为合数。
Time:        2020.1.27
Author:      YaoXie
"""
# while True:
#     a = int(input('Enter a positive integer :\n'))
#     b = int(a ** 0.5)
#     is_prime = True
#     if a <= 1:
#         print("素数是一个大于1的自然数，请重新输入！")
#     if a == 2:
#         print("%d is a prime" % a)
#     else:
#         for i in range(2, b + 1):
#             if a % i == 0:
#                 is_prime = False
#                 print("%d is not a prime" % a)
#                 break
#         if is_prime:
#             print("%d is a prime" % a)
# 关键点：判断时需设置一个判断变量！

"""
Function_3:  输入两个正整数，计算它们的最大公约数和最小公倍数。

最小公倍数：数论中的一种概念，两个整数公有的倍数成为他们的公倍数，
其中一个最小的公倍数是他们的最小公倍数，
同样地，若干个整数公有的倍数中最小的正整数称为它们的最小公倍数
求最小公倍数算法：
最小公倍数=两整数的乘积÷最大公约数

Time:        2020.1.27
Author:      YaoXie
"""
# METHOD_1: 辗转相除法
# while True:
#     a = int(input('a = \n'))
#     b = int(input('b = \n'))
#     m = a
#     n = b
#     while b != 0:
#         c = a % b
#         a = b
#         b = c
#     print("%d 与 %d 的最大公约数是：%d" % (m, n, a))
#     print("%d 与 %d 的最小公倍数是：%d" % (m, n, m*n/a))

# METHOD_2: 相减法
# while True:
#     a = int(input('a = \n'))
#     b = int(input('b = \n'))
#     m = a
#     n = b
#     while b != a:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#     print("%d 与 %d 的最大公约数是：%d" % (m, n, a))
#     print("%d 与 %d 的最小公倍数是：%d" % (m, n, m * n / a))

#  METHOD_3_1: 穷举法
# while True:
#     a = int(input('a = \n'))
#     b = int(input('b = \n'))
#     m = a
#     n = b
#     i = 1
#     while i <= a:
#         if a % i == 0 and b % i == 0:
#             t = i
#         i += 1
#     print("%d 与 %d 的最大公约数是：%d" % (m, n, t))
#     print("%d 与 %d 的最小公倍数是：%d" % (m, n, m * n / t))

# METHOD_3_2: 改进后的穷举法
# while True:
#     a = int(input('a = \n'))
#     b = int(input('b = \n'))
#     m = a
#     n = b
#     i = a
#     while i >= 1:
#         if i % a == 0 and i % b == 0: # 注意！
#             t = i
#         i -= 1
#     print("%d 与 %d 的最大公约数是：%d" % (m, n, t))
#     print("%d 与 %d 的最小公倍数是：%d" % (m, n, m * n / t))

# METHOD_3_2: 骆昊的穷举法
# x = int(input('x = '))
# y = int(input('y = '))
# # 如果x大于y就交换x和y的值
# if x > y:
#     # 通过下面的操作将y的值赋给x, 将x的值赋给y
#     x, y = y, x
# # 从两个数中较的数开始做递减的循环
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break
#
"""
Function_4:  打印三角形图案
靠右：f(x)=i;
靠左：空格=a-i,*=f(x)-(a-i)
居中：f(x)=2*i-1
Time:        2020.1.27~2020.1.28
Author:      YaoXie
"""
while True:
    a = int(input('请输入要打印的行数：\n'))

    #   打印靠左的三角形
    # for i in range(1, a+1):
    #     for j in range(1, i+1):
    #         print("*", end=" ")
    #     print()

    #   打印靠右的三角形
    # for i in range(1, a+1):
    #     for j in range(1, a+1):
    #         if j < a-i+1:
    #             print(" ", end=" ")
    #         else:
    #             print("*", end=" ")
    #     print()

    #   打印靠右的倒三角形
    # for i in range(1, a+1):
    #     for j in range(1, a+1):
    #         if j >= i:
    #             print("*", end=" ")
    #         else:
    #             print(" ", end=" ")
    #     print()

    # 打印居中的三角形
    for i in range(1, a + 1):
        for j in range(1, a-i+1):
            print(" ", end=" ")
        for z in range(1, 2*i):
            print("*", end=" ")
        print()


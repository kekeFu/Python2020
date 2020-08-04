"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
# from random import randint
#
# while True:
#     money = int(input("请输入总赌注："))
#     while money > 0:
#         print('你的总资产为:', money)
#         needs_go_on = False
#         while True:
#             debt = int(input('请下注: '))
#             if 0 < debt <= money:
#                 break
#         first = randint(1, 6) + randint(1, 6)
#         print('玩家摇出了%d点' % first)
#         if first == 7 or first == 11:
#             print('玩家胜!')
#             money += debt
#         elif first == 2 or first == 3 or first == 12:
#             print('庄家胜!')
#             money -= debt
#         else:
#             needs_go_on = True
#
#         while needs_go_on:
#             current = randint(1, 6) + randint(1, 6)
#             print('玩家摇出了%d点' % current)
#             if current == 7:
#                 print('庄家胜')
#                 money -= debt
#                 needs_go_on = False
#             elif current == first:
#                 print('玩家胜')
#                 money += debt
#                 needs_go_on = False
#
#     print('你破产了, 游戏结束!')

"""
    总结：最初自己写的函数没有搞清要什么时候投色子，
并且if ，else 结构掌握的不是很清楚，对条件的分析欠佳，
还需要多多锻炼自己的逻辑分析能力，加油！
"""


"""
Function_1:  实现计算求最大公约数和最小公倍数的函数。
Implement the function that calculates the
greatest common divisor and the least common multiple.

Time:        2020.1.29
Author:      YaoXie
"""

# def gcf1(n1, n2):
#     """ 暴力循环
#     求最大公约数和最小公倍数的函数
#     """
#     z = 1
#     for i in range(1, n1 + 1):
#         if n1 % i == 0 and n2 % i == 0:
#             z *= i
#     print(f'最大公约数: {z},最小公倍数:{int(n1 * n2 / z)}')
#
#
# def gcf2(n1, n2):
#     """ 相减法
#     求最大公约数和最小公倍数的函数
#     """
#     a1 = n1
#     b1 = n2
#     while n2 != 0:
#         if n1 < n2:
#             n1, n2 = n2, n1
#         n1, n2 = n2, n1 - n2
#     print(f'最大公约数: {n1},最小公倍数:{int(a1 * b1 / n1)}')
#
#
# def gcf3(n1, n2):
#     """ 相除法
#     求最大公约数和最小公倍数的函数
#     """
#     a1 = n1
#     b1 = n2
#     while n2 != 0:
#         n1, n2 = n2, n1 % n2
#     print(f'最大公约数: {n1},最小公倍数:{int(a1 * b1 / n1)}')
#
#
# while True:
#     a = int(input("a = "))
#     b = int(input("b = "))
#     gcf1(a, b)
#     gcf2(a, b)
#     gcf3(a, b)

# int(a1 * b1 / n1) 可用 a1 * b1 // n1 代替


"""
Function_2:  判断一个数是不是回文数
Determine if a number is a palindrome

Time:        2020.1.29
Author:      YaoXie
"""
#
#
# def is_palindrome(n1):
#     a = n1
#     t = 0
#     while n1:
#         t = t * 10 + n1 % 10
#         n1 //= 10
#     if a == t:
#         print(f'{a} is a palindrome.')
#     return a == t

# 若仅仅是判断，可以直接写成 return a == t


# while True:
#     a = int(input("a = "))
#     detp(a)

"""
Function_3:  判断一个数是不是素数的函数。
Determine whether a number is a function of prime numbers.

Time:        2020.1.29
Author:      YaoXie
"""
# from math import sqrt
#
#
# def is_primer(n):
#     result = True
#     for i in range(2, int(sqrt(n)) + 1):
#         if n % i == 0:
#             result = False
#             break
#     return result

#
# while True:
#     a = int(input("a = "))
#     print(f'{is_primer(a)}')

"""
Function_4:  写一个程序判断输入的正整数是不是回文素数。
Write a program to determine if the input 
positive integer is a palindrome prime.

Time:        2020.1.29
Author:      YaoXie
"""


# def is_palindrome_primer(n):
#     return is_palindrome(n) and is_primer(n)
#
#
# while True:
#     a = int(input("a = "))
#     print(is_palindrome_primer(a))
#
#
# def foo():
#     global a        # 全局变量
#     a = 200
#     print(a)  # 200
#
#
#     def foo2():
#         c = 1
#
#
#
# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)  # 200

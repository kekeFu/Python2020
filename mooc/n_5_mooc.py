from math import *


def isSqrt(n):
    i = 1
    while n:
        n -= i
        i += 2
    return 0 == n


def perfect_square():
    for i in range(1, 10000):
        a1 = i + 3120
        b1 = i + 1472
        a = a1 % 10
        b = b1 % 10
        if a in [0, 1, 4, 5, 6, 9] and b in [0, 1, 4, 5, 6, 9]:
            if isSqrt(a1) and isSqrt(b1):
                print(i)
        else:
            break


def t1():
    ans = 0
    for i in range(1, 10000):
        tmp1 = int(sqrt(i + 3120))
        tmp2 = int(sqrt(i + 1472))
        if tmp1 ** 2 == int(i + 3120) and tmp2 ** 2 == int(i + 1472):
            ans = i
            break
    print(ans)


def t2():
    """约瑟夫环问题"""
    n = int(input())
    m = int(input())
    humanlist, ans = [], []
    for i in range(0, n):
        humanlist.append(i)
    idx = 0
    for i in range(0, n):
        num = (m + i) % len(humanlist)
        if num == 0:
            num = len(humanlist)
        ans.append(humanlist[(idx + num - 1) % len(humanlist)])
        humanlist.pop((idx + num - 1) % len(humanlist))
        if len(humanlist) == 0:
            break
        idx = (idx + num - 1) % len(humanlist)
    print(ans)


def is_prime(n):
    flag = 1
    for j in range(2, int(n/2)):
        if n % j == 0:
            flag = 0
            break
    return flag


def t3():
    """输出质数"""
    n = int(input())
    t = 0
    while t < 5:
        if is_prime(n):
            if t < 4:
                print(n, end=",")
            else:
                print(n, end="")
            t += 1
        n += 1
    pass


if __name__ == '__main__':
    # perfect_square()
    t1()
    # t2()
    # t3()

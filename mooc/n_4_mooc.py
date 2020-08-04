def t1():
    a = eval(input())
    if isinstance(a, int) and a >= 100:
        for i in range(100, a+1):
            b = i
            s = 0
            while b:
                t = b % 10
                s += t ** 3
                b = b // 10
            if s == i:
                print(i)


def t2():
    a = eval(input())
    if isinstance(a, int) and a > 0:
        for i in range(3, a+1):
            s = 1
            for j in range(2, i):
                if i % j == 0:
                    s = s + j
            if s == i:
                print(s)


def t3():
    a = eval(input())
    if 1 < a < 20:
        j = 0
        for i in range(a, 0, -1):
            print((j * " ")+(2*i-1) * "+")
            j += 1


if __name__ == '__main__':
    # t1()
    # t2()
    t3()
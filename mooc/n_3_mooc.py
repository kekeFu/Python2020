def f1():
    """三次方格式化"""
    a = eval(input())
    print(f'{a**3:#^20}')


def f2():
    s = input()
    a = s[-1]
    b = s[0:-1]
    print(a, b)
    con = b.count(a)
    print(con)


def f3():
    p = input()
    c = ''
    for i in p:
        if i == ' ':
            continue
        t1 = chr(ord(i)+3)
        c += t1
    print(c)


if __name__ == '__main__':
    f1()
    # f2()
    # f3()
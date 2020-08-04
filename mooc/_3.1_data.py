'a good day '


def dayup():
    """天天向上"""
    a1 = pow(1.001, 365)
    a2 = pow(0.999, 365)
    print(f'a1:{a1:.2f}\t a2:{a2:.2f}')
    df = eval(input("请输入一个进步值："))
    up = pow(1+df, 365)
    down = pow(1-df, 365)
    print(f'up:{up:.2f}\t down:{down:.2f}')


def dayup_2(a):
    """
    5+2模式
    :return: result
    """
    d = 1
    for i in range(1, 366):
        if i % 7 in [6, 0]:
            d = d*(1-a)
        else:
            d = d*(1+a)
    print(f'a={a:.3f}, d={d:.2f}')


def dayup_3(df, a):
    d = 1
    for i in range(1, 366):
        if i % 7 in [6, 0]:
            d = d * (1 - a)
        else:
            d = d * (1 + df)
    return d


def dayup_3_2():
    df = 0.01
    while dayup_3(df, 0.01) < 37.78:
        df += 0.001
    print(f'df={df:f}')


def t1():
    a1 = 10
    a2 = 10.0
    b = -10
    b1 = 0b10
    b2 = 0o10
    b3 = 0x10
    print(b1, b2, b3)
    print(round(a2) == a2)
    print(max(a1, a2, b), min(a1, a2, b))
    print(abs(b), divmod(a1, a2))
    print(int(a2), float(a1), complex(b))
    b4 = 1 + 2j
    print(b4.real, b4.imag)


if __name__ == '__main__':
    # dayup_2(0.005)
    # dayup_3_2()
    t1()

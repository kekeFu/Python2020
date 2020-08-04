import time


def t1():
    scale = 10
    print('-------- 执行开始 --------')
    for i in range(scale + 1):
        a = '*' * i
        b = '.' * (scale - i)
        c = (i/scale) * 100
        print(f'{c:^3.0f}% [{a}->{b}]')
    print('-------- 执行结束 --------')


def t2():
    for i in range(101):
        print("\r{:3}%".format(i), end="")
        time.sleep(0.1)
    pass


def t3():
    scale = 50
    print("执行开始".center(scale//2, "-"))
    start = time.perf_counter()
    for i in range(scale+1):
        a = '*' * i
        b = '.' * (scale - i)
        c = (i/scale)*100
        dur = time.perf_counter() - start
        print(f'\r{c:^3.0f}%[{a}->{b}]{dur:.2f}s', end='')
        time.sleep(0.1)
    print("\n"+"执行结束".center(scale//2, "-"))


def t4():
    print("time.time()", time.time())
    print("time.ctime()", time.ctime())
    t = time.gmtime()
    print("time.gmtime()", t)
    print(time.strftime("%Y-%m-%d %H:%M:%S", t))


if __name__ == '__main__':
    # t1()
    # t2()
    # t3()
    t4()

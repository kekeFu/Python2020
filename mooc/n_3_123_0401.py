import time


def text_tag():
    """ DIY"""
    # for i in range(100):
    #     k = 100 - i
    #     # print("{}%->{}".format(i, k * '*'), end="")
    #     print(f'{i:}%->{k:*>10}')

    """ Reference"""
    # scale = 50
    # print("执行开始".center(scale // 2, '-'))
    # start = time.perf_counter()
    # for i in range(scale + 1):
    #     a = '*' * i
    #     b = '.' * (scale - i)
    #     c = (i / scale) * 100
    #     dur = time.perf_counter() - start
    #     print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end='')
    #     time.sleep(0.1)
    # print("\n" + "执行结束".center(scale // 2, '-'))

    """ Try_2"""
    # r 可以让光标移到最前，因为执行速度很快，必须休眠一下才能看到变化，注意细节的处理！
    scale = eval(input())
    print("执行开始".center(scale // 2, "-"))
    start = time.perf_counter()
    for i in range(scale+1):
        percent = (i / scale) * 100
        left = '*' * i
        right = '.' * (scale-i)
        dur = time.perf_counter() - start
        print(f'\r{percent:^3.0f}%[{left:}->{right:}]{dur:.2f}s', end="")
        time.sleep(0.1)
    print("\n"+"执行结束".center(scale // 2, "-"),)


def tree_power():
    """三次方格式化 ，{t :-^20}，填充+方式+宽度"""
    n = eval(input())
    if isinstance(n, int) or isinstance(n, float):
        t = pow(n, 3)
        print(f'{t :-^20}')


def start_triangle():
    """ R
    槽中可以嵌套槽，用来表示宽度、填充等含义。
    """
    n = eval(input())
    for i in range(1, n + 1, 2):
        print("{0:^{1}}".format('*' * i, n))


def entry():
    """ 恺撒密码
    用到了chr(),ord()函数，
    """
    s = input()
    t = ""
    for c in s:
        if 'a' <= c <= 'z':
            t += chr(ord('a') + ((ord(c) - ord('a')) + 3) % 26)
        elif 'A' <= c <= 'Z':
            t += chr(ord('A') + ((ord(c) - ord('A')) + 3) % 26)
        else:
            t += c
    print(t)


if __name__ == '__main__':
    # text_tag()
    # tree_power()
    start_triangle()

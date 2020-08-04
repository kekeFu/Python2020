def t1():
    """
    温度转换：Temperature conversion
    """
    t = input('请输入要转换的温度值：')
    if t[-1] in ['f', 'F']:
        c = (eval(t[0:-1])-32) * 5 / 9
        print('转换后的温度是{:.2f}C'.format(c))
    elif t[-1] in ['c', 'C']:
        f = 1.8 * eval(t[0:-1]) + 32
        print('转换后的温度是{:.2f}F'.format(f))
    else:
        print('输入有误！')


def t2():
    """
    慕课堂测试题，eval()
    """
    r = eval(input("请输入一个有效的表达式：\n"))
    print(r)


if __name__ == '__main__':
    t2()

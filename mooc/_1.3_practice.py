def t1():
    x, y = 10, [10, 20, 30]
    print(x is y)   # False
    print(x in y)   # True


def t2():
    """
    变量命名问题
    :return: wu
    """
    园2 = 1
    # 1a = 1
    # print(园2, 1a)
    pass


def t3():
    user = input("请输入你的用户名：")
    passwd = input("请输入你的密码：")
    if user == "admin" and passwd == "000":
        print("恭喜你，登录成功")
    else:
        print("用户名或密码错误")
    # pass


def t4():
    t = input('请输入要转换的温度值：')
    if t[-1] in ['f', 'F']:
        c = (eval(t[0:-1]) - 32)/1.8
        print('转换后的温度是{:.2f}C'.format(c))
    elif t[-1] in ['c', 'C']:
        f = 1.8 * eval(t[0:-1]) + 32
        print('转换后的温度是{:.2f}F'.format(f))
    else:
        print('输入有误！')


if __name__ == '__main__':
    # t1()
    # t3()
    t4()

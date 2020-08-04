def select():
    t = pow(-1, 0.5)
    print(t)
    name = "Python语言程序设计课程"
    print(name[0], name[2:-2], name[-1])
    s = 'PYTHON'
    print("{0:3}".format(s))
    pass


def square_root():
    a = eval(input())
    b = pow(a, 0.5)
    print(f'{b:+>30.3f}')
    pass


def str_segmentation():
    s = input()
    a = s.split('-')
    # print(a)
    # s.split("s中的分割符"),此函数会返回一个列表！
    print(a[0]+"+"+a[-1])


def a1(x):
    a = 1.0
    for i in range(366):
        if i % 7 in [0, 6]:
            a = a*(1 - 0.01)
        else:
            a = a*(1 + x)
    print(a)
    return a


def dayt():
    b = pow(1.01, 365)
    x = 0.01
    while a1(x) < b:
        x += 0.001
    print(x)


if __name__ == '__main__':
    # select()
    # square_root()
    # str_segmentation()
    dayt()
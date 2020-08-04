import turtle as t


def octagon():
    """ 绘制一个八边形 """
    t.pensize(2)
    t.up()
    t.fd(-100)
    t.pd()
    for i in range(8):
        t.fd(100)
        t.left(45)
    t.done()


def t2():
    """ Octagonal graphics """
    t.pensize(2)
    t.up()
    t.fd(-100)
    t.pd()
    for i in range(8):
        t.fd(150)
        t.left(135)
    t.done()


if __name__ == '__main__':
    # octagon()
    t2()
import turtle as t


def t1():
    """绘制多个同切圆"""
    for i in range(4):
        t.pensize(i**2)
        t.circle(20*i)
        t.pencolor('red')
    t.done()


def t2():
    """绘制五角星"""
    t.pu()
    t.bk(100)
    t.pd()
    t.color('red', 'red')
    t.begin_fill()
    for i in range(5):
        t.fd(200)
        t.rt(144)
        # t.right(144)      # 两个right 就是五边形
    t.end_fill()
    t.done()


def t3():
    t.pu()
    t.fd(-100)
    t.pd()
    t.pencolor("red")
    for i in range(3):
        t.circle(-90, 90)
        t.circle(90, -90)
    t.done()
    t.fd(100)


if __name__ == '__main__':
    # t1()
    # t2()
    t3()
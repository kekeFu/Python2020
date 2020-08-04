import turtle as t


def pentagram():
    """绘制五角星"""
    t.pu()
    t.bk(100)
    t.pd()

    t.color('black', 'red')
    t.begin_fill()
    for i in range(5):
        t.fd(200)
        t.rt(144)
    t.end_fill()
    t.done()


def draw_python():
    """ 蟒蛇 """
    t.pu()
    t.fd(-250)
    t.pd()
    t.pensize(40)
    t.pencolor("purple")
    t.seth(-40)
    for i in range(4):
        t.circle(40, 80)
        t.circle(-40, 80)
    t.circle(40, 40)
    t.fd(40)
    # t.angle()
    t.circle(26, 180)
    t.done()


def h1(a, b):
    t.pu()
    t.goto(a, b)
    t.seth(0)
    t.pd()
    pass


def bagua_map():
    t.color('black', 'black')

    t.begin_fill()
    t.circle(100, -180)
    h1(0, 0)
    t.circle(-100, 180)
    h1(0, -200)
    t.circle(200, 180)
    t.end_fill()

    h1(0, -200)
    t.circle(200, -180)

    t.color('black', 'white')
    t.begin_fill()
    h1(0, 90)
    t.circle(10)
    t.end_fill()

    t.color('black', 'black')
    t.begin_fill()
    h1(0, -90)
    t.circle(10)
    t.ht()
    t.end_fill()

    t.done()
    pass


if __name__ == '__main__':
    t.title("48-谢瑶-201826705050")
    # draw_python()
    # pentagram()
    bagua_map()

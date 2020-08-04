import turtle as t


def draw_python():
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
    t.circle(40, 180)
    t.done()


def square():
    t.pensize(2)
    for i in range(4):
        t.lt(90)
        t.fd(-200)
    t.done()


def hexagon():
    """ 六边形 """
    t.pensize(2)
    for i in range(6):
        t.lt(60)
        t.fd(100)
    t.done()


def folded_edge():
    """ 叠边形 """
    t.pensize(2)
    for i in range(9):
        t.fd(200)
        t.lt(80)
    t.done()


def wind_mill():
    """ 风轮 """
    t.pensize(2)

    t.circle(100, -45)
    t.goto(0, 100)
    t.fd(100)
    t.pu()
    t.goto(0, 0)
    t.seth(0)

    for i in range(1, 4):
        t.circle(100, -90 * i)
        t.pd()
        t.circle(100, -45)
        t.goto(0, 100)
        t.fd(100)
        t.pu()
        t.goto(0, 0)
        t.seth(0)

    t.pd()
    t.goto(0, 200)
    t.pu()
    t.goto(-100, 100)
    t.pd()
    t.goto(100, 100)

    t.done()


if __name__ == '__main__':
    draw_python()
    # square()
    # hexagon()
    # folded_edge()
    # wind_mill()
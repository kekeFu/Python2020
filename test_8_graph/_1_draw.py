import turtle


def t1():
    """
    绘制蟒蛇（Python drawing）
    """
    # setup() 设置启动窗体及大小
    turtle.setup(650, 350, 200, 200)

    # 让海龟飞起
    turtle.penup()

    # 让海龟往后飞250，到达屏幕中间左边
    turtle.fd(-250)

    # 让海龟落地
    turtle.pendown()

    # 给海龟设置腰围为25
    turtle.pensize(25)

    # 给海龟设置颜色为黄色
    turtle.pencolor("green")

    # 让海龟顺时针转40度，绝对角度
    turtle.seth(-40)

    # 让海龟开始以半径40，正向转80度，反向转80度
    for i in range(4):
        turtle.circle(40, 80)
        turtle.circle(-40, 80)
    turtle.circle(40, 80/2)
    turtle.fd(40)
    turtle.circle(16, 180)
    turtle.fd(40 * 2/3)

    # 保持图形
    turtle.done()


def t2():
    """海龟角度绘制  z """
    turtle.setup(600, 600)
    turtle.left(45)
    turtle.fd(150)
    turtle.right(135)
    turtle.fd(300)
    turtle.left(135)
    turtle.fd(150)
    turtle.done()


def t3():
    """绝对角度绘制  z """
    turtle.setup(600, 600)
    turtle.seth(45)
    turtle.fd(150)
    turtle.seth(-90)
    turtle.fd(300)
    turtle.seth(45)
    turtle.fd(150)
    turtle.done()


def t4():
    """画个圆"""
    turtle.setup(800, 800)
    turtle.circle(100, 480)


if __name__ == '__main__':
    t1()
    # t4()
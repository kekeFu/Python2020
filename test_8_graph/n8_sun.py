"""
Date:   2020-3-12

"""
from turtle import *


def sun(i):
    title(i)
    pu()
    bk(100)
    pd()
    write("By YaoXie", align="left", font=("Arial", 8, "normal"))
    # 主图
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(i)
        if abs(pos()) < 1:
            break
    end_fill()
    done()


if __name__ == '__main__':
    i = 150
    sun(i)


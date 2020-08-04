"""
else:没有异常时执行的代码
finally: 无论是否异常都执行的代码，例如：关闭文件
"""


def t1():
    try:
        print(1)
    except Exception as r:
        print(r)
    else:
        print('我是else，当无异常时执行的代码')


def t2():
    try:
        f = open('text.txt', 'r')
    except Exception as r:
        print(r)
        f = open('text.txt', 'w')
    else:
        print('没有异常！')
    finally:
        print('关闭文件')
        f.close()


if __name__ == '__main__':
    # t1()
    t2()

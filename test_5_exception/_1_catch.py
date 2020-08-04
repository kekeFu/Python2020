"""
异常：错误，bug
处理异常：尝试执行某句可能出现异常的语句，
         若出错则用正确的代码去替代。

try:
    可能发生错误的代码
except：
    如果出现异常执行的代码
"""


def t1():
    try:
        f = open('test.txt', 'r')
    except:
        f = open('test.txt', 'w')


def t2():
    try:
        b.bar()
    except:
        class Car(object):
            def bar(self):
                print("刹车")


        b = Car()
        b.bar()


if __name__ == '__main__':
    t2()


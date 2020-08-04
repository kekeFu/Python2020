"""
Date：2020-2-27

function：
    格式化输出
    1.初始 %
    2.format()

参考文章：
1.https://finthon.com/python-format/
2.
"""


def t1():
    """ %s，%d，%f """
    age = 18
    name = 'Tom'
    weight = 70.5
    stu_id = 1
    stu_id2 = 230
    print('%03d' % stu_id)      # 001
    print('%03d' % stu_id2)     # 230
    print('%s, %03d' % (name, age+1))
    print('%.2f' % weight)      # 70.00


def t2():
    """
    f'string'
    """
    age = 18
    name = 'Tom'
    weight = 70.5
    print('%s, %s, %s' % (name, age, weight))
    #  Tom, 18, 70.5
    print(f'My name is {name}')
    print(f'My name is {name:^10}')
    print(f'My name is {"Tom":^10}')
    print('My name is {:^10}'.format('Tom'))


def t3():
    """
    format()
    1.顺序匹配
    2.自定义顺序匹配
    3.键值匹配
    4.字典方式匹配
    """
    print('hello {}, my name is {}'
          ''.format('everyone', 'python'))

    print('hello {1}, my name is {0}'
          ''.format('everyone', 'python'))

    print('hello {b}, my name is {a}'
          ''.format(a='everyone', b='python'))

    x = {'a': 'everyone', 'b': 'python'}
    print('hello {a}, my name is {b}'
          ''.format(**x))


def t4():
    """
    format()
    对齐方式和填充
    1.填充
    2.无填充
    :return: 无

    """


if __name__ == '__main__':
    # t2()
    t3()

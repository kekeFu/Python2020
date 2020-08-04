"""
类属性（Class attribute）
    定义：类对象所拥有的属性，被该类的所有实列对象所共有
         类对象和实例对象皆可访问类属性
    应用条件：记录的某项数据始终保持一致，可将其定义为类属性
    对比：类属性为全类共有，创建多个对象，类属性只需一份内存空间；
         实例属性 要求每个对象都要单独开辟一片内存空间

修改类属性： 类属性只能由类对象来访问修改，实例对象无法修改
"""


class Dog(object):
    tooth = 10


def main():
    dah = Dog()
    print(Dog.tooth)    # 10
    print(dah.tooth)    # 10

    dah.tooth = 12
    print(Dog.tooth)    # 10
    Dog.tooth = 12
    print(Dog.tooth)    # 12
    print(dah.tooth)    # 12


if __name__ == '__main__':
    main()
"""
类方法（Class method）：
    特点：需用装饰器 @classmethod 来标识类方法，
         第一个参数必须为类对象，默认 cls 为第一个参数
    应用：方法中需使用类对象（访问私有类属性），则定义类方法
         类方法一般与类属性配合使用
"""


class Dog(object):
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth


def main1():
    dah = Dog()
    t = dah.get_tooth()
    print(t)


"""      
静态方法（Static method）
    特点：通过装饰器 @staticmethod 来修饰，
         不需要传递类对象或者实例对象
         形参没有 self/cls
         可通过实例对象和类对象去访问
    应用：取消不需要的参数传递，
         减少不必要的内存占用和性能消耗
"""


class Dog2(object):
    @staticmethod
    def info_print():
        print('这是静态方法。')


def main2():
    da = Dog2()
    da.info_print()
    Dog2.info_print()


if __name__ == '__main__':
        main2()

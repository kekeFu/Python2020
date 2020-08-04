"""
多态：一类事物有多种形态，一个抽象类有多个子类，
     子类重写父类方法，调用不同子类的相同父类方法
"""


class Dog(object):
    def work(self):
        print('指哪打哪……')


class EnemyDog(Dog):
    def work(self):
        print('追击敌人……')


class DrugDog(Dog):
    def work(self):
        print('追查毒品……')


class NewDog(EnemyDog, DrugDog):
    pass


class Person(object):
    def work_with_dog(self, dog):
        # 传入对象，将对象作为参数传入
        dog.work()


def main():
    ad = EnemyDog()
    dd = DrugDog()
    daqiu = Person()
    daqiu.work_with_dog(ad)
    daqiu.work_with_dog(dd)


if __name__ == '__main__':
    main()


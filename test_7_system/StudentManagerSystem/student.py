class Student(object):
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'姓名：{self.name},' \
               f'性别：{self.gender},' \
               f'手机号：{self.tel}'

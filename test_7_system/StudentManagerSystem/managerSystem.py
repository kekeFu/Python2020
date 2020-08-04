"""
存储数据：文件（student.data）
        加载文件数据
        修改数据后保存到文件
存储形式：list 存储学员对象
系统功能：add,del,modify,find,display,save,exit
"""
from student import *


class StudentManager(object):
    def __init__(self):
        """存储数据"""
        self.stu_list = []

    def run(self):
        self.load_stu()

        while True:
            self.show_menu()
            k = int(input('请输入功能序号：\n'))
            if k == 1:
                self.add_stu()
            elif k == 2:
                self.del_stu()
            elif k == 3:
                self.modify()
            elif k == 4:
                self.find()
            elif k == 5:
                self.display()
            elif k == 6:
                self.save()
            elif k == 7:
                break

    @staticmethod
    def show_menu():
        """显示功能菜单"""
        print('请选择如下功能：')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员')
        print('5:显示全部学员信息')
        print('6.:保存学员信息')
        print('7:退出系统')

    def add_stu(self):
        name = input('请输入您的姓名：')
        gender = input('请输入您的性别：')
        tel = input('请输入您的电话号码：')
        stu = Student(name, gender, tel)
        self.stu_list.append(stu)
        print(self.stu_list, stu)

    def del_stu(self):
        del_name = input('请输入要删除学员姓名：')
        for i in self.stu_list:
            if i.name == del_name:
                self.stu_list.remove(i)
                break
        else:
            print('查无此人。')
        print(self.stu_list)

    def modify(self):
        modiy_name = input('请输入要修改的学员姓名：')
        for i in self.stu_list:
            if i.name == modiy_name:
                i.name = input('请输入您的姓名：')
                i.gender = input('请输入您的性别：')
                i.tel = input('请输入您的电话号码：')
                print(f'姓名：{i.name},性别：{i.gender},电话号码：{i.tel}\n'
                      f'修改学员信息成功.')
                break
        else:
            print('该学员不存在！')

    def find(self):
        find_name = input('请输入要修改的学员姓名：')
        for i in self.stu_list:
            if i.name == find_name:
                print(f'姓名：{i.name},性别：{i.gender},电话号码：{i.tel}\n'
                      f'修改学员信息成功.')
                break
        else:
            print('该学员不存在！')

    def display(self):
        for i in self.stu_list:
            print(f'姓名：{i.name},'
                  f'性别：{i.gender},'
                  f'电话号码：{i.tel}\n'
                  f'修改学员信息成功.')

    def save(self):
        """文件写入学员数据"""
        f = open('student.data', 'w')
        new_list = [i.__dict__ for i in self.stu_list]
        f.write(str(new_list))
        f.close()

    def load_stu(self):
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            data = f.read()

            # 将data字符串转换为列表类型数据
            new_list = eval(data)

            # 列表推导式
            self.stu_list = [Student(i['name'],
                                     i['gender'],
                                     i['tel'] )
                             for i in new_list]
        finally:
            f.close()
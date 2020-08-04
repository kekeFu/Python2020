"""
Function_1: Student Management System
功能：
    1.添加学员
    2.删除学员
    3.修改学员信息
    4.查询
    5.显示所有学员
    6.退出系统
分析：
    1.全局变量，数据类型为列表    info = []
    2.需求分析：接受，保存，判断，

# 显示功能界面
# 用户输入功能序号
# 根据用户输入，执行不同的功能（函数）

Date:       20202.2.3~20202.2.4
Author:     YaoXie
"""


# 定义函数
def interface():
    print('欢迎来到学员管理系统！')
    print('1.添加学员')
    print('2.删除学员')
    print('3.修改学员信息')
    print('4.查询学员信息')
    print('5.显示所有学员信息')
    print('6.退出系统')
    print('-' * 20)


# 定义一个list全局变量存储所有数据，存储值为字典
info = [{'name': 'a', 'id': '1', 'tel': 'a1'},
        {'name': 'b', 'id': '2', 'tel': 'b2'},
        {'name': 'c', 'id': '3', 'tel': 'c3'}]


# 添加学员信息
def add():
    """
    添加学员信息函数
    :return:
    """
    new_name = input('请输入要添加学员的姓名：')
    new_id = input('请输入id：')
    new_tel = input('请输入电话号码：')

    # 判断输入的 id 是否存在
    for i in info:
        if new_id == i['name']:
            print('您输入的 id 已存在')
            return

    #  定义一个空字典来暂时存储输入的信息
    temp_dict = {'name': new_name, 'id': new_id, 'tel': new_tel}
    info.append(temp_dict)
    print(info)


# 删除学员信息
def delete():
    del_id = input('请输入要删除学员你的 id 号：')
    for i in info:
        if del_id == i['id']:
            info.remove(i)
            return
    print('学员不存在！')


# 修改学员信息
def modify():
    mod_id = input('请输入要修改学员的 id 号：')
    for i in info:
        if mod_id == i['id']:
            mod_name = input('请输入修改后的名字：')
            mod_tel = input('请输入修改后的电话号码：')
            i['name'] = mod_name
            i['tel'] = mod_tel
            return
    print('学员信息不存在！')


# 查询学员信息
def query():
    que_name = input('请输入要查询学员的 姓名：')
    for i in info:
        if que_name == i['name']:
            print(i)


def print_all():
    for i in info:
        print(f"姓名：{i['name']}\t"
              f"id：{i['id']}\t"
              f"电话号码{i['tel']}")
        # 注意f'{}'中引号用法


# 用户输入
t = True
interface()
while t:
    a = int(input('请选择功能序号：\n'))
    if a == 6:
        print('退出系统！')
        t = False
    elif a == 1:
        add()
    elif a == 2:
        delete()
    elif a == 3:
        modify()
    elif a == 4:
        query()
    elif a == 5:
        print_all()
    else:
        print('请选择1~6中的一个数字来进行下步操作。')




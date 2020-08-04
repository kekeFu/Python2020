# -*- coding: utf-8 -*-
# @Time    : 2020/4/22/0022
# @Author  : Yann
# @File    : student.py
# @Software: PyCharm

# 用来保存学生所有信息的列表
stuInfo = []
newName = ''
newSex = ''
newPhone = ''


# 开始提示
def printMenu():
    print('=' * 30)
    print('\t学生管理系统')
    print('1-添加学生', '2-删除学生', '3-修改学生')
    print('4-查询学生', '5-查询所有学生')
    print('=' * 30)


# 获得学生信息
def getStuInfo():
    # 全局变量的修改需要先声明
    global newName
    global newSex
    global newPhone
    newName = input('输入姓名')
    newSex = input('输入年龄')
    newPhone = input('输入电话')
    return [newName, newSex, newPhone]


# 完成功能1
def addStuInfo():
    result = getStuInfo()
    # 新建字典
    newInfo = {}
    newInfo['name'] = result[0]
    newInfo['sex'] = result[1]
    newInfo['phone'] = result[2]
    # 列表里面加字典
    stuInfo.append(newInfo)
    print('添加成功')


# 完成功能2
def delStuInfo():
    id = int(input('学生序号'))
    stuInfo.remove(stuInfo[id - 1])
    print('删除成功')


# 完成功能3
def updStuInfo():
    id = int(input('学生序号'))
    result = getStuInfo()
    stuInfo[id - 1]['name'] = result[0]
    stuInfo[id - 1]['sex'] = result[1]
    stuInfo[id - 1]['phone'] = result[2]
    print('修改完成')


# 完成功能4
def indStuInfo():
    id = int(input('学生序号'))
    print('name:', stuInfo[id - 1]['name'], 'sex:', stuInfo[id - 1]['sex'], 'phone:', stuInfo[id - 1]['phone'])
    print('查询成功')


# 完成功能5
def indAllStuInfo():
    for i in stuInfo:
        print('name:', i['name'], 'sex:', i['sex'], 'phone:', i['phone'])
    if len(stuInfo) == 0:
        print('没有学生信息，请添加！')


# 测试
if __name__ == '__main__':
    while True:
        print('请选择：')
        printMenu()
        id = int(input('请选择：'))
        if id == 1:
            addStuInfo()
        elif id == 2:
            delStuInfo()
        elif id == 3:
            updStuInfo()
        elif id == 4:
            indStuInfo()
        elif id == 5:
            indAllStuInfo()
        else:
            print('输入错误')



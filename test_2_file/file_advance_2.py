"""
文件或文件夹操作:
    1.rename(), 重命名
    2.remove(), 删除
文件夹操作:
    1.mkdir()，创建文件夹
    2.rmdir()，删除文件夹
    3.getcwd()，获取当前文件夹路径
    4.chdir(目录)，改变默认目录, 并定位到指定目录
    4.listdir(目录)，获取目录列表

总结：批量处理文件命名容易出错，最好不要缺省参数
"""
import os

# os.rename('test1.txt', 't.txt')
# os.remove('test2.txt')
# os.mkdir('a')
# os.rmdir('a')

# print(os.getcwd())

# os.chdir('a')
# os.mkdir('b')

# print(os.listdir('a'))
# os.rename('a', 'aa')

"""
测试案例，批处理重命名文件
获取最初文件名，确定字符串要插入最初文件名的位置，
创建新文件名，重命名
"""
path = r'D:\Users\ASUS\PycharmProjects\test_2_beifen'
fifle_list = os.listdir(path)
print(fifle_list)
for i in fifle_list:
    old_name = i
    new_name = 'py_' + i
    print('旧文件名：%-20s,新文件名：%-20s' % (old_name, new_name))
    # os.rename(i, new_name)

"""
恢复: 修改seting（interpret），
修改文件夹名字(运行一下会产生一个新的.idea文件，并且报错)
在有venv（虚拟环境）的情况下，非常容易出错！
"""
# path = r'D:\Users\ASUS\PycharmProjects\test_2_beifen'
# fifle_list = os.listdir(path)
# print(fifle_list)
# for i in fifle_list:
#     old_name = i
#     num = len('py_')
#     new_name = i[num:]
#     print('旧文件名：%-20s,新文件名：%-20s' % (old_name, new_name))
#     os.rename(i, new_name)

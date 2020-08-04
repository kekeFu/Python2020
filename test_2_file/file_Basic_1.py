"""
文件操作：存储数据，
        1.打开 open(name, mode)
        name: 可以打开已有的文件，或直接创建
        mode: 访问模式，只读，写入，追加等
        2.读写 f.write('a')，f.read(num)
        3.关闭 f.close()

访问模式 mode:可省略（文件存在），默认表示 r
    1. 文件指针放在开头，r：只读；rb：以二进制的格式；r+：
    2. w, 从头写入（会覆盖原有的数据），
    3. a, 追加

"""
# f = open('test.txt', 'wb+')
# f.write(bytes(10))
# # f.write('aaa')
# f.close()

"""
f.read(), f.readlines(), f.readline()
"""
# read(num),不写参数则默认读取所有
# f = open('test.txt', 'r+')
# f.write('abc')
# print(f.read())
# f.close()

# f.readlines()，按行的方式把整个文件的内容一次性读取，返回一个列表
# f = open('test.txt', 'r')
# c = f.readlines()
# print(c)
# f.close()

# f.readline()，一次读取一行
# f = open('test.txt', 'r')
# c = f.readline()    # abc
# print(c)
# c = f.readline()    # vbz
# print(c)
# f.close()

"""
测试：r+, w+, a+ 区别
1. r+: 文件不存在则会报错，文件指针在文件开始，即从头读到尾，只能读
2. w+: 文件不存在则新建一个文件，文件指针在文件开始，新内容会覆盖旧内容
3. a+: 文件不存在则新建一个文件，文件指针在文件结尾，无法读取
"""
# f = open('test1.txt', 'r+')
# c = f.read()
# print(c)
# f.close()

# f = open('test1.txt', 'w+')
# f.write('ada')
# c = f.read()
# print(c)
# f.close()

# f = open('test.txt', 'a+')
# f.write('c')
# f.close()

"""
f.seek(偏移量，起始位置),移动文件指针
0:文件开头
1：当前位置
2：文件结尾
"""
# f = open('test.txt', 'r+')
# f.seek(0, 2)
# c = f.read()
# print(c)
# f.close()

# f = open('test.txt', 'a+')
# f.seek(1, 0)
# c = f.read()
# print(c)
# f.close()

# f = open('test.txt', 'w+')
# f.write('ad')
# f.seek(0, 0)
# c = f.read()    # ad
# print(c)
# f.close()

"""
文件备份，例：test[备份].txt
步骤：
    1.接受用户输入的目标文件名
    2.规划备份文件名， 提取目标特点-后缀，名字与后缀分离
    3.将旧文件写入到备份文件中
"""
# old_name = input("请输入备份文件名：")
# index = old_name.rfind('.')
#
# if index > 0:
#     postfix = old_name[index:]
#
# new_name = old_name[:index] + '[备份]' + postfix
# # print(new_name)
#
# old_f = open(old_name, 'rb')
# new_f = open(new_name, 'wb')
# while True:
#     c = old_f.read(1024)
#     if len(c) == 0:
#         break
#     new_f.write(c)
#
# old_f.close()
# new_f.close()

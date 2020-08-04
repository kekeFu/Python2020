"""
查缺补漏_1：三目运算符
"""
# a = 1
# b = 2
# c = a - b if a > b else b - a   # 从左开始运算
# print(c)

'''
查缺补漏_2：字符串
'''
# 初步认识
# a = 'hello \n world'
# b = '''hello world'''
# c = "I'm Tom."
# d = 'I\'m Tom.'
# print(type(a), type(b))
# print(a)
# print(b, c)

# 字符串输出
# name = 'rose'
# print('我的名字是：%s' % name)
# print(f'My name is {name}')
# 字符串输入
# password = input("您输入的密码的是：\n")
# print(password, type(password))

# 下标，索引，编号：通过下标快速找到数据;从 0 开始编号
# str1 = 'acvd'
# for i in range(len(str1)):
#     print(i, str1[i])
# 切片,截取一部分字符，[start, end, step]
# str1 = 'acvd'
# print(str1[:])              # 选取所有
# print(str1[1:3:2])          # 不包含结束
# print(str1[::-1])           # dvca,默认步长为 1
# print(str1[0:len(str1)])    # acvd，不包含结束
# print(str1[-1:-4:-1])       # 选取方向一致！

# 字符串常用方法：查找 （find，index，count，rfind, rindex ）
# s1 = 'If you cannot accept now,'
# print(s1.find('ca', 1, 15))     # 7
# print(s1.find('-1'))            # 不存在，则返回 -1
# print(s1.index('ca', 1, 15))    # 7
# # print(s1.index('-1'))           # 报错
# print(s1.count('c'))            # 4, 返回出现次数
# print(s1.count('i'))            # 不存在，则返回 0

# 修改，替换replace(a, b, count) , split,join
# s1 = 'you also cannot meet tomorrow!'
# new_s1 = s1.replace('c', 's', 10)
# print(s1)       # 字符串为不可变类型，
# print(new_s1)   # replace 有返回值

# new_s2 = s1.split('al')     # 丢失分割字符
# print(new_s2)
# s2 = ['a', 'b', 'c']
# new3_s2 = ''.join(s2)  # 连接字符
# print(new3_s2)

# capitalize() , title(),
# s1 = 'hello world!'
# print(s1.capitalize())      # 首字母大写
# print(s1.title())           # 每个单词大写
# # lower(),upper()
# print(s1.lower())           # 大写转小写
# print(s1.upper())           # 大写转小写

# s1 = '   hello world!   '
# print(s1)
# print(s1.lstrip())      # 删除左侧空白
# print(s1.rstrip())      # 删除右侧空白
# print(s1.strip())       # 删除两侧空白

# s1 = 'hello world!'
# print(s1.ljust(20, '.'))     # ljust(字符数，'填充字符')，左对齐
# print(s1.rjust(20, '*'))     # rjust(字符数，'填充字符')，左对齐
# print(s1.center(20, ' '))     # center(字符数，'填充字符')，左对齐

# 判断 startswith()
s1 = 'hello world 123!'
# print(s1.startswith('he', 0, 10))   # True
# print(s1.endswith('ld', 0, 10))     # False
# print(s1.isalpha())         # False，判断是否全由字母组成
# print(s1.isdigit())         # False，判断是否全由数字组成
# print(s1.isalnum())         # False，判断是否全由字母和数字组成
# print(s1.isspace())           # False，判断是否全由空格组成
print(s1.isascii())  # False，判断是否全由字母组成
help(s1.isascii())

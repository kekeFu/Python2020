"""
Function_Preview:  字符串和常用数据结构.
Python中的字符串有两种索引方式，
从左往右以0开始，从右往左以-1开始。
Time:        2020.1.30
Author:      YaoXie
"""
# s1 = '\'hello, world!\'\n'
# s2 = "\\hello, world!\n"
# # 以三个双引号或单引号开头的字符串可以折行
# s3 = """
# hello,
# world!
# """
# print(s1, s2, s3, end='')

# s1 = '\141\142\143\x61\x62\x63'     # abcabc
# # \后面还可以跟一个八进制或者十六进制数来表示字符
# s2 = '\u9a86\u660a'         # 骆昊
# print(s1, s2)
#
# s1 = r'\'hello, world!\''
# # 加上 r 可以让 \ 不表示转义
# s2 = r'\n\\hello, world!\\\n'
# print(s1, s2, end='')
#


"""
+ : 字符串拼接
* ：字符串重复
in : 判断字符串是否在另一字符串中
[] or [:] : 提取字符串，切片运算
"""
# s1 = 'hello ' * 3
# print(s1)   # hello hello hello
# s2 = 'world'
# s1 += s2
# print(s1)   # hello hello hello world
# print('llo h' in s1)   # True
# print('good' in s1)     # False
# str2 = 'abc123456'
# # 从字符串中取出指定位置的字符(下标运算)
# print(str2[2])  # c ,默认从 0 开始索引
# # 字符串切片(从指定的开始索引到指定的结束索引)
# print(str2[2:5])    # c12
# print(str2[2:])     # c123456 缺省时自动补齐
# print(str2[2::2])   # c246 从第3个数字开始加 2
# print(str2[::2])    # ac246 从第 1 个数字开始加 2
# print(str2[::-1])   # 654321cba 从最后 1 个数字开始从右向左 -1
# print(str2[-3:-1])  # 45 从倒数第 2 个数字开始从左向右移到倒数第 2个数

"""
常用的一些关于字符串的内置函数：
len():长度, capitalize(): 首字母大写, title():单词首字母大写, 
upper():所有字母大写
find(): 默认从 0 开始索引，寻找字符串位置  
index与find类似，但寻找失败会报错
startswith() or endswith(): 判断字符串开始或结束是否以指定的字符匹配
center() or rjust():将字符串以指定的宽度居中或靠右并在两侧填充指定的字符
isdigit() or isalpha() or isalnum():检查字符串是否由数字或字母或两者混合构成
strip()：将字符串中左右两边的空格去除
"""
# str1 = 'hello, world!'
# # 通过内置函数len计算字符串的长度
# print(len(str1))    # 13
# # 获得字符串首字母大写的拷贝，就是将字符串首字母转成大写
# print(str1.capitalize())    # Hello, world!
# # 获得字符串每个单词首字母大写的拷贝，将字符串中每个单词首字母大写
# print(str1.title())     # Hello, World!
# # 获得字符串变大写后的拷贝，将字符串所有字母大写
# print(str1.upper())     # HELLO, WORLD!
# # 从字符串中查找子串所在位置
# print(str1.find(' '))  # 6
# print(str1.find('shit'))    # -1，不发生异常
#
# # index与find类似，但找不到子串时会引发异常！
# print(str1.index(' '))      # 6
# # print(str1.index('shit'))
#
# # 检查字符串是否以指定的字符串开头
# print(str1.startswith('He'))    # False
# print(str1.startswith('hel'))   # True
# # 检查字符串是否以指定的字符串结尾
# print(str1.endswith('!'))   # True
#
# # 将字符串以指定的宽度居中并在两侧填充指定的字符
# print(str1.center(50, '*'))
# # 将字符串以指定的宽度靠右放置左侧填充指定的字符
# print(str1.rjust(50, ' '))
#
# str2 = 'abc123456'
# # 检查字符串是否由数字构成
# print(str2.isdigit())  # False
# # 检查字符串是否以字母构成
# print(str2.isalpha())  # False
# # 检查字符串是否以数字和字母构成
# print(str2.isalnum())  # True
#
# str3 = '  jackfrued@126.com '
# print(str3)
# # 获得字符串修剪左右两侧空格之后的拷贝，将字符串中的空格去除
# print(str3.strip())

"""
字符串输出，常用有三种
"""
# a, b = 5, 10
# print('%d * %d = %d' % (a, b, a * b))
# # .format 可以调用不同位置的数
# print('{0} * {1} = {2}'.format(a, b, a * b))
# print(f'{a} * {b} = {a * b}')

"""
列表：另一些常用的 结构化的、非标量类型——列表（list：有序序列）
"""
# list1 = [1, 3, 5, 7, 100]
# print(list1)    # [1, 3, 5, 7, 100]
# # 乘号表示列表元素的重复
# list2 = ['hello'] * 3
# print(list2)    # ['hello', 'hello', 'hello']
# # 计算列表长度(元素个数)
# print(len(list1))   # 5
# # 下标(索引)运算
# print(list1[0])     # 1
# print(list1[4])     # 100
# # print(list1[5])   # IndexError: list index out of range
# print(list1[-1])    # 100
# print(list1[-3])    # 5
# list1[2] = 300
# print(list1)    # [1, 3, 300, 7, 100]
#
# # 通过循环用下标遍历列表元素
# for index in range(len(list1)):
#     print(list1[index])
# # 通过for循环遍历列表元素
# for elem in list1:
#     print(elem)
# # 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
# for index, elem in enumerate(list1):
#     print(index, elem)
#
# fruits = ['grape', 'apple', 'strawberry', 'waxberry']
# fruits += ['pitaya', 'pear', 'mango']
# # 列表切片
# fruits2 = fruits[1:4]
# # 索引为 1，第 4 个元素结束，即取 4-1 个元素
# f = fruits[1:5]
# print(f, fruits2)
# print(fruits2)  # apple strawberry waxberry
# # 可以通过完整切片操作来复制列表
# fruits3 = fruits[:]
# print(fruits3)  # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
#
# fruits4 = fruits[-3:-1]
# print(fruits4) # ['pitaya', 'pear']
# # 可以通过反向切片操作来获得倒转后的列表的拷贝
# fruits5 = fruits[::-1]
# # print(fruits5) # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']

""" 排序 """
# list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# list2 = sorted(list1)
# # sorted函数返回列表排序后的拷贝不会修改传入的列表
# # 函数的设计就应该像sorted函数一样尽可能不产生副作用
# list3 = sorted(list1, reverse=True)
# # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
# list4 = sorted(list1, key=len)
# print(list1)
# print(list2)    # 按字母排序
# print(list3)    # 逆序
# print(list4)    # 长度从短到长
# # 给列表对象发出排序消息直接在列表对象上进行排序
# list1.sort(reverse=True)
# print(list1)    # 逆序

"""
    生成式和生成器
    一般法，yield 法    
"""

# import sys
#
# f = [x for x in range(1, 10)]
# print(f)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# f = [x + y for x in 'ABCDE' for y in '1234567']
# print(f)
# # ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
# # 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7',
# # 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7',
# # 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7',
# # 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7']
#
# # 用列表的生成表达式语法创建列表容器
# # 用这种语法创建列表之后，元素已经准备就绪，所以需要耗费较多的内存空间
# f = [x ** 2 for x in range(1, 1000)]
# print(sys.getsizeof(f))  # 查看对象占用内存的字节数
# print(f)
#
# # 请注意下面的代码创建的不是一个列，表而是一个生成器对象
# # 通过生成器可以获取到数据但它不占用额外的空间存储数据
# # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
# f = (x ** 2 for x in range(1, 1000))
# print(sys.getsizeof(f))
# # 相比生成式生成器，这个表而个生成器对象不占用存储数据的空间
# print(f)
# for val in f:
#     print(val)


# def fib(n):
#     """斐波拉切数列的生成器"""
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a
#
#
# def main():
#     for val in fib(20):
#         print(val)
#
#
# if __name__ == '__main__':
#     main()

# 定义元组
# t = ('骆昊', 38, True, '四川成都')
# print(t)
# # 获取元组中的元素
# print(t[0])
# print(t[3])
# # 遍历元组中的值
# for member in t:
#     print(member)
# 重新给元组赋值
# t[0] = '王大锤'  # TypeError,元组的元素不能修改!

# 变量t重新引用了新的元组原来的元组将被垃圾回收
# t = ('王大锤', 20, True, '云南昆明')
# print(t)
# # 将元组转换成列表
# person = list(t)
# print(person)
# # 列表是可以修改它的元素的
# person[0] = '李小龙'
# person[1] = 25
# print(person)
# # 将列表转换成元组
# fruits_list = ['apple', 'banana', 'orange']
# fruits_tuple = tuple(fruits_list)
# print(fruits_tuple)

"""
总结：元组适用与一些不用增删改的情况，
比如构造安全的 多线程环境或须返回多个值，
元组时间和空间的利用率高于列表
"""

"""
集合：创建，使用——增删改，
"""
# 创建集合的字面量语法
# set1 = {1, 2, 3, 3, 3, 2}
# print(set1)     # 不允许重复元素！
# print('Length =', len(set1))
# 此时不需要格式控制符，因为len是函数

# # 创建集合的构造器语法(面向对象部分会进行详细讲解)
# set2 = set(range(1, 10))
# set3 = set((1, 2, 3, 3, 2, 1))
# print(set2, set3)
# # 创建集合的推导式语法(推导式也可以用于推导集合)
# set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
# print(set4)
#
# # 向集合添加元素和从集合删除元素。
# set1.add(4)
# set1.add(5)
# set2.update([11, 12])       # 添加元素
# set2.discard(5)             # 从集合删除元素 5
# if 4 in set2:               # 从集合删除元素 4
#     set2.remove(4)
# print(set1, set2)
# print(set3.pop())           # pop() 移除列表中的一个元素（默认第一个元素），并且返回该元素的值。
# print(set3)
#
# # 集合的交集、并集、差集、对称差运算
# print(set1 & set2)      # 求交集
# print(set1.intersection(set2))
# print(set1 | set2)      # 求并集
# print(set1.union(set2))
# print(set1 - set2)      # 求差集
# print(set1.difference(set2))
# print(set1 ^ set2)      # 求对称差集
# print(set1.symmetric_difference(set2))
#
# # 判断子集和超集
# print(set2 <= set1)
# # print(set2.issubset(set1))
# print(set3 <= set1)
# # print(set3.issubset(set1))
# print(set1 >= set2)
# # print(set1.issuperset(set2))
# print(set1 >= set3)
# # print(set1.issuperset(set3))

"""
字典是另一种可变容器模型:
以键值对的形式可以存储任意类型对象, 
"""
# 创建字典的字面量语法
# scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
# print(scores)
# # 创建字典的构造器语法
# items1 = dict(one=1, two=2, three=3, four=4)
# # 通过zip函数将两个序列压成字典
# items2 = dict(zip(['a', 'b', 'c'], '123'))
# # 创建字典的推导式语法
# items3 = {num: num ** 2 for num in range(1, 10)}
# print(items1, items2, items3)
# # 通过键可以获取字典中对应的值
# print(scores['骆昊'])
# print(scores['狄仁杰'])
# # 对字典中所有键值对进行遍历
# for key in scores:
#     print(f'{key}: {scores[key]}')
# # 更新字典中的元素
# scores['白元芳'] = 65
# scores['诸葛王朗'] = 71
# scores.update(冷面=67, 方启鹤=85)
# print(scores)
# if '武则天' in scores:
#     print(scores['武则天'])
# print(scores.get('武则天'))
# # get方法也是通过键获取对应的值但是可以设置默认值
# print(scores.get('武则天', 60))
# # 删除字典中的元素
# print(scores.popitem())
# print(scores.popitem())
# print(scores.pop('骆昊', 100))
# # 清空字典
# scores.clear()
# print(scores)

# 在屏幕上显示跑马灯文字。
# # import os
# import time
#
#
# def main():
#     content = '北京欢迎你为你开天辟地…………'
#     while True:
#         # 清理屏幕上的输出
#         os.system('cls')  # os.system('clear')
#         print(content)
#         # 休眠200毫秒
#         time.sleep(0.2)
#         content = content[1:] + content[0]
#
#
# if __name__ == '__main__':
#     main()



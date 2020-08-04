"""
function_1: list
date:       2020.2.2~2020.2.3
author:     YaoXie
"""
# list1 = ['name', 'age', 'sex']
# # 查找
# print(list1[0], list1[1])   # name age
# print(list1.index('name'))  # 0
# print(list1.count('tom'))   # 0
# print(len(list1))       # len 是公共函数

# 判断指定数据在某个序列
# list1 = ['name', 'age', 'sex']
# print('name' in list1)          # True
# print('names' not in list1)     # True

# list1 = ['Tom', 'Lily', 'Sandy']
# name1 = input('请输入账号：\n')
# if name1 in list1:
#     print('用户名已经存在')
# else:
#     print('注册成功！')
#     list1.append(name1)
# print(list1)

# 追加数据，append, extend, insert
# list1 = ['Tom', 'Lily', 'Sandy']
# print(list1)
# list1.append(['1', '2'])
# # ['Tom', 'Lily', 'Sandy', ['1', '2']]
# print(list1)
# list1.extend('esdt')
# # ['Tom', 'Lily', 'Sandy', ['1', '2'], 'e', 's', 'd', 't']
# print(list1)
# list1.insert(1, 'aa')
# # ['Tom', 'aa', 'Lily', 'Sandy', ['1', '2'], 'e', 's', 'd', 't']
# print(list1)

# 删除，del, pop, remove, clear
# list1 = ['Tom', 'Lily', 'Sandy', 'Andy']
# del(list1[0])           # del可删除指定下标的数据
# print(list1)            # ['Lily', 'Sandy', 'Andy']
# print(list1.pop())      # Andy, pop函数有返回值
# print(list1)            # pop 函数默认删除最后一个
# list1.remove('Lily')
# print(list1)
# print(list1.clear())    # None，无返回值
# print(list1)            # []

# 嵌套列表
# a = ['a', 'b', 'c']
# n = ['1', '2', '3']
# x = [a, n]

# 函数：len(list),max,min(),list(元组)
# 方法：list.append(),count,index,pop,reverse,sort,clear,copy

"""
function_2: summary 
len(), del()/del , max min, 

date:       2020.2.2~2020.2.3
author:     YaoXie
"""
# str1 = 'absce'
# list1 = [1, 2, 3, 4]
# tuple1 = (1, 2, 3, 4)
# set1 = {1, 2, 3, 4}
# dict1 = {'1': 'a', '2': 'b', '3': 'c'}
# print(len(str1), len(list1), len(tuple1), len(set1), len(dict1))
# del str1
# del(list1[0])
# print(list1)
# del tuple1
# print(tuple1)
# del (dict1['1'])
# print(dict1)

# print(max(list1))       # 返回最大值
# print(min(list1))

# range(start, end, step), 与 for 一起使用, 不包含 end 数据
# for i in range(5):
#     print(i, end=' ')   # 0 1 2 3 4
# print()
# for i in range(1, 5):
#     print(i, end=' ')   # 1 2 3 4
# print()
# for i in range(1, 5, 2):
#     print(i, end=' ')   # 1 3

# enumerate(可遍历对象， start=0) ,组合一个可遍历的数据对象为索引序列
# list1 = ['a', ['b', 'c'], 'd']
# for i in enumerate(list1):
#     print(i)





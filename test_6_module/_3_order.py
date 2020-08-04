"""
导入一个模块，Python解释器对模块位置搜索顺序： 由进及远
      1.当前目录
      2.搜shell变量PYTHONPATH下的目录
      3.查看默认路径，UNIX下，默认一般为/user/local/lib/python
注意：
      1.自定义模块不与已有模块名重名，若重复，则无法使用；
      2.若自定义于导入的功能重名，则调用后写的功能
"""
# import random
# num = random.randint(1, 5)
# print(num)

# from time import sleep

# def sleep():
#     print('1')

# sleep()

"""
扩展：重名的严重性
Python，引用传递数据
1.命名后者会覆盖前者，和模块重名的变量会覆盖功能
"""
import time
print(time)         # <module 'time' (built-in)>
# time = 1
# print(time)         # 1

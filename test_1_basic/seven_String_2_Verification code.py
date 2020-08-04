"""
Function_Exercise:
设计一个函数产生指定长度的验证码，
验证码由大小写字母和数字构成。

Time:        2020.1.31
Author:      YaoXie
"""
import random
# import string
#
#
# def gvc(n=3):
#     if n < 3:
#         return '输入长度不能小于3'
#     str = ''
#     while n:
#         place = random.randint(1, 3)
#         print(place)
#         if place == 1:
#             str1 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#             str += str1
#         if place == 2:
#             str2 = random.choice('abcdefghijklmnopqrstuvwxyz')
#             str += str2
#         if place == 3:
#             str3 = random.choice('0123456789')
#             str += str3
#         n -= 1
#     return str
#
#
# a = int(input("请输入要生成的验证码数：\n"))
# x = gvc(a)
# print(x)

'''
总结，还行，大力还有改进的余地！
请看以下代码
'''


# def generate_code(code_len=4):
#     """
#     生成指定长度的验证码
#     :param code_len: 验证码的长度(默认4个字符)
#     :return: 由大小写英文字母和数字构成的随机验证码
#     """
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)
#         code += all_chars[index]    # 巧妙之处在于设置了索引！
#     return code



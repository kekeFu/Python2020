"""
Function_1:  华氏温度转换为摄氏温度。
Time:        2020.1.27
Author:      YaoXie
# """
# Fahrenheit = int(input("please input an number:\n"))
# Celsius = float((Fahrenheit - 32) * 5 / 9)
# # print("华氏温度:%4d,\n转换为摄氏温度:%4.2f" % (Fahrenheit, Celsius))
# print(f'{Fahrenheit} 华氏度 = {Celsius} 摄氏度')

"""
Function_2:  输入圆的半径计算计算周长和面积。
Time:        2020.1.27
Author:      YaoXie
"""
# import math
#
# radius = float(input(" Enter the radius: \n "))
# perimeter = 2 * radius * math.pi
# area = math.pi * radius * radius
# print(math.pi)
# print(" radius = %.2f,\n perimeter = %.2f,\n area = %.2f" % (radius, perimeter, area))
#

"""
Function_3:  输入年份判断是不是闰年。
Time:        2020.1.27
Author:      YaoXie
"""
year = int(input(" Enter the year: \n"))
t1 = year % 100
t2 = year % 4
t3 = year % 400
is_leap = ((t1 != 0 and t2 == 0) or t3 == 0)
print(is_leap)

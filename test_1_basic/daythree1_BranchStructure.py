"""
Function_1:  分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
Time:        2020.1.27
Author:      YaoXie
"""
import math

# x = float(input("Please input number : \n "))
# if x > 1:
#     y = 3 * x - 5
# elif -1 <= x <= 1:
#     y = x + 2
# else:
#     x < -1
# print(" x = %.2f,\n y = %.2f" % (x, y))

"""
Function_2:  英制单位英寸和公制单位厘米互换.
Time:        2020.1.27
Author:      YaoXie
"""
# in1 = float(input("Input a number: \n"))
# cm = 2.54 * in1
# unit = input("请输入单位：\n ")
# if unit == 'inch' or unit == '英寸':
#     print("%.2f 英寸 = %.2f 厘米" % (in1, cm))
# else:
#     if unit == 'cm' or unit == '厘米':
#         print("%.2f 厘米 = %.2f 英寸" % (cm, in1))
#     else:
#         print('请输入有效的单位')

"""
Function_3:  百分制成绩转换为等级制成绩。
要求：
    如果输入的成绩在90分以上（含90分）输出A；
    80分-90分（不含90分）输出B；
    70分-80分（不含80分）输出C；
    60分-70分（不含70分）输出D；
    60分以下输出E。
Time:        2020.1.27
Author:      YaoXie
"""
# METHOD1: 使用elseif , 如果可以简单点会更好
# Percentage = float(input('Enter a Percentage:\n'))
# graded = Percentage / 10
#
# if graded >= 9:
#     print("A")
# elif graded == 8:
#     print("B")
# elif graded == 7:
#     print("C")
# elif graded == 6:
#     print("D")
# elif graded < 6:
#     print("E")
# else:
#     print("输入有误！")

"""
Function_4:  输入三条边长，如果能构成三角形就计算周长和面积。
Time:        2020.1.27
Author:      YaoXie
"""
# METHORD1
side1 = float(input("请输入第一条边长：\n"))
side2 = float(input("请输入第二条边长：\n"))
side3 = float(input("请输入第三条边长：\n"))
a = [side1, side2, side3]
b = sorted(a)
if b[0] > b[2] - b[1] and b[2] < b[0] + b[1]:
    print(b)
    perimeter = b[0] + b[2] + b[1]
    print("周长 = %.2f" % perimeter)
    perimeter /= 2
    area = math.sqrt(perimeter * (perimeter - b[0]) * (perimeter - b[1]) * (perimeter - b[2]))
    print("面积 = %.2f" % area)
else:
    print("不能构成三角形！")
# 注意三角形成立的条件：
# 1.1 三边都大于0
# 1.2 任意两边之和大于第三边，或，任意两边之差小于第三边

# METHORD2
# if a + b > c and b + c > a and c + a > b
# if a > c -b and b > a - c and c > b - a

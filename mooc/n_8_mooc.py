# ctrl + alt + L 格式化

from pip._vendor.distlib.compat import raw_input


def f(s, a):
    t = 0
    s1 = []
    for i in s:
        if t < a:
            s1.append(i)
            t += int(i)
    return s1


def sumup(list1):
    s = 0
    for i in list1:
        s += i
    return s


def test1(a, sum1, list1):
    flag = -1
    s = 0
    lis1 = []
    if int(4 * a) == sum1:
        for i in list1:
            if i < s:
                s += i
                lis1.append(i)
            elif i == s:
                flag = 0
                lis1.append(i)
            
    return flag


if __name__ == '__main__':
    list1 = []
    str = raw_input()
    lst1 = str.split(" ")  # lst1用来存储输入的字符串，用空格分割
    sum1 = 0
    for i in lst1[1:]:
        list1.append(int(lst1.pop()))
    sum1 = sumup(list1)
    a = sum1 // 4
    test = test1(a, sum1, list1)
    if test == 0:
        print("y")
    else:
        print("n")
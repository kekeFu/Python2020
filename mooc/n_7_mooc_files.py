def csv1():
    """ 按行进行倒序排列；‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬"""
    f = open("data.txt", "r")
    s = f.readlines()
    s.reverse()
    f.close()
    f = open("newdata1.txt", "w")
    for line in s:
        f.write(line)
    f.close()
    pass


def csv2():
    """ 每行数据倒序排列；‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬"""
    f1 = open("data.txt", "r")
    s = f1.readlines()
    f1.close()
    f2 = open("newdata2.txt", "w")
    for line in s:
        f2.write(line[::-1])
    f2.close()
    pass


def csv3():
    """ 使用分号（;）代替逗号（,）分割数据，无空格；"""
    f1 = open("data.txt", "r")
    s = f1.readlines()
    f1.close()
    f2 = open("newdata3.txt", "w")
    for line in s:
        t = line.replace(",", ';')
        t = t.replace(' ', '')
        f2.write(t)
    f2.close()
    pass


def cvs4():
    """ 综合"""
    f = open('data.txt', 'r')
    lines = f.readlines()
    lines.reverse()
    f.close()

    f2 = open("newdata4.txt", "w")
    for line in lines:
        line = line.replace(' ', '')
        line = line.replace(",", ';')
        f2.write(line[::-1])
    f2.close()


def t1():
    f = open("a.txt")
    s = 0
    for line in f:
        line = line.strip('\n')
        if len(line) == 0:
            continue
        s += 1
    print("共{}行".format(s))


def t2():
    f = open("a.txt")
    cc = 0
    d = {}
    for i in range(26):
        d[chr(ord('a') + i)] = 0
    for line in f:
        for c in line:
            d[c] = d.get(c, 0) + 1
            cc += 1
    print("共{}字符".format(cc), end="")
    for i in range(26):
        print(",{}:{}".format(chr(ord('a') + i), d[chr(ord('a') + i)]), end="")


if __name__ == '__main__':
    # t1()
    t2()
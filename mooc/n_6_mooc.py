def t1():
    """ 合并两个列表并去重"""
    alist = list(map(int, input().split()))
    blist = list(map(int, input().split()))
    s = list(set(alist+blist))
    t = sorted(s)
    print(t)


def t2():
    """ 字典"""
    alist = list(map(int, input().split()))
    l = int(len(alist) / 2)
    a = str(alist[0])
    b = str(alist[1])
    d = {}
    d[a] = alist[0:l]
    d[b] = alist[l:]
    print(str(d).replace(str(d[a]), str(d[a]).replace(' ', '')).replace(str(d[b]), str(d[b]).replace(' ', '')))


def t3():
    import math
    alist = list(map(int, input().split()))
    t = sorted(alist, key=lambda k: math.fabs(k))
    print(str(t).replace(' ', ''))
    pass


if __name__ == '__main__':
    # t1()
    # t2()
    t3()
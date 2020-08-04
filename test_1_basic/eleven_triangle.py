"""
杨辉三角
"""


def c0(n=1):
    s = 1
    for i in range(1, n+1):
        s *= i
    # print(f'A({n}) = {s}')
    if n <= 0:
        s = 0
    return s


def c1(n, m):
    if n == 0 or m == 0:
        c = 0
    elif n == m:
        c = 1
    else:
        c = c0(n) // c0(m) // c0(n-m)
    # print(f'C({n},{m}) = {c}')
    return c


# 出现了点问题，第3个测试数据开始出错
def yh_triangle_vio(n=1):
    for i in range(1, n+1):
        # for j in range(i, n-i+1):
        #     print(' ', end=' ')
        for j in range(1, i+1):
            if j == 1 or j == i:
                t = 1
            else:
                t = c1(i-1, j) + c1(i-1, j-1)
            print("%3d" % t, end=' ')
        print()


def yh_triangle(n=1):
    # num = int(input('Number of rows: '))
    yh = [[]] * n
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


def main():
    n = int(input('请输入要测试的案例数：'))
    t = 1
    while t <= n:
        # yh_triangle(t)
        yh_triangle_vio(t)
        print()
        t += 1


if __name__ == '__main__':
    main()

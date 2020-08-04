""" 基本统计值计算"""


def getNum():
    nums = []
    iNumStr = input("请输入数字（回车退出）：")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字（回车退出）：")
    return nums


def mean(numbers):
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)


def dev(numbers, mean):
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return pow(sdev / (len(numbers)-1), 0.5)


def median(numbers):
    new = sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (new[size//2 - 1] + new[size//2]) / 2
    else:
        med = new[size/2]
    return med


if __name__ == '__main__':
    n = getNum()
    m = mean(n)
    print(f'平均值：{m}，标准差：{dev(n,m):.2}，中位数：{mean(n)}')
def temperature_transfer():
    str1 = input()
    if str1[-1] in ['c', 'C']:
        F = eval(str1[0:-1]) * 1.8 + 32
        print(f'{F:.2f}F')
    elif str1[-1] in ['f', 'F']:
        C = (eval(str1[0:-1]) - 32) / 1.8
        print(f'{C:.2f}C')
    else:
        print('输入有误！')


def temperature_transfer_2():
    str1 = input()
    if str1[0] in ['c', 'C']:
        F = eval(str1[1:]) * 1.8 + 32
        print(f'F{F:.2f}')
    elif str1[0] in ['f', 'F']:
        C = (eval(str1[1:]) - 32) / 1.8
        print(f'C{C:.2f}')
    else:
        print('输入有误！')


def money_change():
    str1 = input()
    if str1[:3] in ['RMB']:
        USD = eval(str1[3:]) / 6.78
        print(f'USD{USD:.2f}')
    elif str1[:3] in ['USD']:
        RMB = eval(str1[3:]) * 6.78
        print(f'RMB{RMB:.2f}')
    else:
        print()


if __name__ == '__main__':
    # temperature_transfer()
    # temperature_transfer_2()
    money_change()
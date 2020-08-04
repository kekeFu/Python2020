def f1():
    a = 10
    print(hex(a), oct(a), chr(a), ord(chr(a)))
    print("1 + 1 = 2 \t" + chr(10004))
    for i in range(12):
        print(ord(chr(9800 + i)), chr(9800 + i), end=" ")
    print(10 * '*', '*' * 10)


s1 = '  aV bCSID EW '


def f2():
    print(len(s1))
    print(s1.lower(), s1.upper())
    print(s1.replace('a', '1', 2))
    print(s1.strip())
    print(s1.center(20, '*'))
    print(s1.split(' ', 2))     # ['', '', 'aV bCSID EW ']
    print(s1.count('a'))
    print(','.join(s1))
    print(s1)


def f3():
    s = 111222333
    print(f"{s:=^20}")
    print(f'{s:*>20}')
    print(f'{s:$<20}')
    print(f'{s:-^30,.2%}')
    print(f'{s:*>30,.2f}')
    print(f'{s:$<30x}')


if __name__ == '__main__':
    f1()
    # f2()
    # f3()
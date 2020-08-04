def cubic_Format():
    n = eval(input())
    if isinstance(n, int):
        print("{:#^20d}".format(n**3))
    elif isinstance(n, float):
        print('{:#^20f}'.format(n**3))


def cubic_Format_1():
    n = eval(input())
    if isinstance(n, int):
        n = str(pow(n, 3))
        print(n.center(20, '#'))
    elif isinstance(n, float):
        n = str(pow(n, 3))
        print(n.center(20, '#'))


def count_characters():
    s = input().split(' ')
    print(s[0].count(s[1]))


def encrypt_Craesar():
    p = input()
    c = ''
    for i in p:
        if 'a' <= i <= 'z':
            c += chr(ord('a') + (ord(i)-ord('a')+3) % 26)
        elif 'A' <= i <= 'Z':
            c += chr(ord('A') + (ord(i)-ord('A')+3) % 26)
    print(c)


if __name__ == '__main__':
    # cubic_Format_1()
    # count_characters()
    encrypt_Craesar()

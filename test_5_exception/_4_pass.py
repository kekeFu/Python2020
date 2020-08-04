"""
异常传递（Exception passing）：
异常时可以嵌套书写的，由外到内

案例1：1.尝试只读打开test.txt 文件，有内容存在则读取，无则提示用户
      2.循环读取，无内容时退出循环，若文件意外终止，则提示用户
"""
import time

try:
    f = open('text.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        # 在命令提示符中按 ctrl + c ，进行测试
        print('意外终止读取数据')
    finally:
        f.close()
        print('关闭文件')
except:
    print('文件不存在')


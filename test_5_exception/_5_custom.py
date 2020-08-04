"""
自定义异常（Custom exception）
用来报错，不合逻辑的错
案例1：密码长度不足，则报错。
      1.自定义异常
      2.用 raise 异常类对象，来抛出异常的描述信息
      3.捕获异常
"""


class ShortInputError(Exception):
    """
    自定义异常类，继承Exception
    """
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    def __str__(self):
        """
        设置抛出异常的描述信息
        """
        return f'您输入的密码长度是{self.length},' \
               f'不能小于最小长度 {self.min_len}'


def main1():
    try:
        code = input('请输入密码：\n')
        if len(code) < 3:
            # 抛出异常类创建对象
            raise ShortInputError(len(code), 3)
    except Exception as r:
        # 捕获该异常
        print(r)
    else:
        print('密码已输入完成')


if __name__ == '__main__':
    main1()

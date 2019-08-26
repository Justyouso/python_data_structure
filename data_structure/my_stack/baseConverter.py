# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-8-20 下午9:12

from pythonds.basic.stack import Stack


def baseConverter(decNumber, base):
    """
    功能：将十进制装换成任意进制数
    实现：remainder=decNumber%base,压入栈,decNumber=decNumber//base,直到decNumber<=0
    :param decNumber: 十进制数
    :param base: 需要转换的进制
    :return: str
    """

    digits = '0123456789ABCDEF'
    stack = Stack()
    result = ''
    while decNumber > 0:
        remainder = decNumber % base
        stack.push(digits[remainder])
        decNumber = decNumber // base

    while not stack.isEmpty():
        result = result + str(stack.pop())

    return result


print(baseConverter(100, 16))

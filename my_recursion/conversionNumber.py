# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-5 下午4:41


def toStr(num, base):
    """
    功能:转换成任意进制
    实现:递归实现,取商递归,加上余数
    :param num: 
    :param base: 
    :return: 
    """
    convertString = '0123456789ABCDEF'

    if num < base:
        return convertString[num]
    else:
        return toStr(num // base, base) + convertString[num % base]


num = 10
base = 2
print(toStr(num, base))

# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-8-26 上午9:51

from pythonds.basic.deque import Deque


def palchecker(aString):
    """
    功能:回文字符串检测,如:'adsda','asddsa'
    实现:使用双向队列(deque)实现,将字符串加入双向队列,循环取首尾字符比对,直到队列长度不大于1
    :param aString: 回文字符串
    :return: bool
    """
    chardeque = Deque()
    for i in aString:
        chardeque.addRear(i)
    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        front = chardeque.removeFront()
        rear = chardeque.removeRear()
        if front != rear:
            stillEqual = False

    return stillEqual


print(palchecker('asdasa'))

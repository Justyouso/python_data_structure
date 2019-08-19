# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-8-16 上午10:08


def anagramSolution1(s1, s2):
    """
    功能: 乱序字符串检查,'heart'和'earth'就是乱序字符串,为了简单,规定字符串具有相同的长度
    实现: 将s2转换成列表alist,检查s1中的每个字符是否存在alist中,如果存在,替换成None
    :param s1: 字符串
    :param s2: 字符串
    :return: bool
    """
    alist = list(s2)
    pos1 = 0
    stillok = True
    while pos1 < len(s1) and stillok:
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == s2[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            pos1 += 1
            alist[pos2] = None
        else:
            stillok = False
    return stillok


# print(anagramSolution1('hear1', 'earth'))


def anagramSolution2(s1, s2):
    """
    功能: 乱序字符串检查,'heart'和'earth'就是乱序字符串,为了简单,规定字符串具有相同的长度
    实现: 对比两个字符串中每个字符出现的次数.创建两个长度为26元素值为0的列表c1,c2.分别遍历s1,s2,
    给字符(装换成int)对应在c1,c2中的位置元素进行+1赋值
    :param s1: 字符串
    :param s2: 字符串
    :return: bool
    """
    c1 = [0] * 26
    c2 = [0] * 26
    for i in s1:
        pos1 = ord(i) - ord('a')
        c1[pos1] += 1
    for i in s2:
        pos2 = ord(i) - ord('a')
        c2[pos2] += 1

    stillok = True
    for i, v in enumerate(c1):
        if v != c2[i]:
            stillok = False
            break

    return stillok


print(anagramSolution2('heart', 'earth'))

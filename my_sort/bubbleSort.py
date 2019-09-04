# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-2 上午10:13


def bubbleSort(alist):
    """
    功能:冒泡排序,一次筛选出一个最大值
    实现:以index的方式遍历列表,每次交换排序出最大的数值
    :param alist: 需要排序的列表
    :return: 
    """
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print(alist)

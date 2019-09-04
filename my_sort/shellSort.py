# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-3 上午10:07

def shellSort(alist):
    """
    功能:希尔排序,希尔排序是插入排序的变种,只需要计算出增量和开索引,再调用插入排序即可
    :param alist: 
    :return: 
    """
    # 计算增量
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        # 调用插入排序
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    """
    功能:加有增量的插入排序
    :param alist: 
    :param start: 
    :param gap: 
    :return: 
    """
    for index in range(start + gap, len(alist), gap):
        currentvalue = alist[index]
        position = index
        while position != 0 and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentvalue

# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-2 下午1:59


def selectionSort(alist):
    """
    功能:选择排序(冒泡排序的变种),选择最大值,记录index,与列表末尾值交换
    实现:以index遍历alist,定义标识positionOfMax记录最大值的index,比较值,
    若location值(当前index)大于positionOfMax值,则positionOfMax=location
    :param alist: 需要排序的列表
    :return: 
    """
    # 从末尾开始,每次处理一个最大数值
    for fillslot in range(len(alist) - 1, 0, -1):
        # 定义一个最大值的index
        positionOfMax = 0
        # 从1-fillslot
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                # 赋值最大值的index
                positionOfMax = location
        # 将最大值和列表末尾值交换赋值
        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[
            fillslot]


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(alist)
print(alist)

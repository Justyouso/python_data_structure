# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-2 下午2:41


def insertionSort(alist):
    """
    功能:插入排序,在列表的较低位置维护一个排序的子列表。然后将每个新项 “插入” 回先前的子列表,
    使得排序的子列表称为较大的一个项
    实现:遍历列表,currentvalue=alist(index),position = index
        1. 循环比较,挪动位置(position = position - 1),
        直到position=0或alist[position-1]<=currentvalue
        (while position != and alist[position-1]>currentvalue)
        2. 将currentvalue插入列表(alist[position] = currentvalue)
        
    使用currentvalue(alist[index])与alist[position-1](position=index)
    循环比较,直到position=0或alist[position-1]<=currentvalue
    :param alist: 数值列表
    :return: 
    """
    # 从1开始(因为第一个元素是有序的)
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        # 挪动位置
        while position != 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1
        alist[position] = currentvalue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(alist)
print(alist)

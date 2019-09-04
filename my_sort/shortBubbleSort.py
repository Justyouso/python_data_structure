# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-2 上午11:31


def shortBubblueSort(alist):
    """
    功能:短冒泡排序(当列表在某一刻为有序时,则不需要进行循环排序)
    实现:
    :param alist: 
    :return: 
    """
    stop = True
    passnum = len(alist) - 1
    while passnum > 0 and stop:
        # 如果没有交换则认为是有序的,不用再进行循环
        stop = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                stop = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum = passnum - 1


alist = [5, 6, 1, 2, 3]
shortBubblueSort(alist)
print(alist)

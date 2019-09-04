# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-4 下午4:30


def quickSort(alist):
    quickHelperSort(alist, 0, len(alist) - 1)


def quickHelperSort(alist, first, last):
    splitpoint = partition(alist, first, last)
    quickHelperSort(alist, first, splitpoint - 1)
    quickHelperSort(alist, splitpoint + 1, last)


def partition(alist, first, last):
    # 取出基准数
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last
    stop = False
    while not stop:
        while alist[leftmark] <= pivotvalue and leftmark <= rightmark:
            leftmark = leftmark + 1

        while leftmark <= rightmark and alist[rightmark] >= pivotvalue:
            rightmark = rightmark - 1
        # 需要循环处理,直到rightmark<leftmark
        if rightmark < leftmark:
            stop = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[
                leftmark]
    # 将基准移到中间位置
    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    return rightmark

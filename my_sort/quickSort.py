# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-4 上午11:41


def quickSort(alist):
    """
    功能:快速排序,
        1.在数据集之中,选择一个元素作为"基准"(pivot)
        2.所有小于"基准"的元素,都移到"基准"的左边;所有大于"基准"的元素,都移到"基准"的右边
        3.对"基准"左边和右边的两个子集,不断重复第一步和第二步,直到所有子集只剩下一个元素为止
    实现:列表中选一个数pivotvalue,从两端遍历列表
        左边:找到大于pivotvalue的数alist[leftmark]
        右边:找到小于pivotvalue的数alist[rightmark]
        将alist[leftmark]和alist[rightmark]交换,并返回基准坐标,用作划分子集
    :param alist: 
    :return: 
    """
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        # 排序并获取中间数位置
        splitpoint = partition(alist, first, last)
        # 从开始位置到中间数位置
        quickSortHelper(alist, first, splitpoint - 1)
        # 从中间数位置到结束位置
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        # 从左开始,直到找到大于pivotvalue
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        # 从右开始,直到找到小于pivotvalue
        while alist[rightmark] >= pivotvalue and leftmark <= rightmark:
            rightmark = rightmark - 1
        # 需要循环处理,直到rightmark<leftmark
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[
                leftmark]
    # 将基准移到中间位置
    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    return rightmark


alist = [18, 13, 12, 16, 10, 85, 65]
quickSort(alist)
print(alist)

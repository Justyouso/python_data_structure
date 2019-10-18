# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-25 下午4:31


def mergeSort(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    left = alist[:mid]
    right = alist[mid:]
    ll = mergeSort(left)
    lr = mergeSort(right)

    return mergeData(ll, lr)


def mergeData(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print(mergeSort(alist))
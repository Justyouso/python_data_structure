# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-5 下午2:36


def binarySearch(alist, item):
    found = False
    first = 0
    last = len(alist) - 1
    while first < last and not found:
        mid = (first + last) // 2
        if alist[mid] == item:
            found = True
        else:
            if alist[mid] > item:
                last = mid - 1
            else:
                first = mid + 1
    return found


alist = [1, 2, 3, 4, 6, 7, 8, 9]
item = 5
print(binarySearch(alist, item))

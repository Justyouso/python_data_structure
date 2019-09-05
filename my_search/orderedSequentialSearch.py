# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-5 下午2:26


def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            pos += 1
    return found

alist = [1, 2, 3, 4, 6, 7, 8, 9]
item = 5
print(orderedSequentialSearch(alist, item))

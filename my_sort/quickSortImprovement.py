# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-25 下午3:57


def quickSort(alist):
    if len(alist) <= 1:
        return alist

    left, right = [], []
    avg = alist.pop()
    for i in alist:
        if i <= avg:
            left.append(i)
        else:
            right.append(i)
    return quickSort(left) + [avg] + quickSort(right)


alist = [18, 13, 12, 16, 10, 85, 65]
print(quickSort(alist))

# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-4 下午2:42

def recursion(num):
    if len(num) == 1:
        return num[0]
    return num[0] + recursion(num[1:])

print(recursion([1,2,3]))
# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-5 上午10:23


def mergeSort(alist):
    """
    功能:归并排序
    实现:
        1.把 n 个记录看成 n 个长度为 l 的有序子表
        2.进行两两归并使记录关键字有序，得到 n/2 个长度为 2 的有序子表
        3.重复第 2 步直到所有记录归并成一个长度为 n 的有序表为止。
    :param alist: 
    :return: 
    """
    print("Splittiing", alist)

    # 递归结束标识
    if len(alist) > 1:
        # 将列表二分
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        # 递归调用
        mergeSort(lefthalf)
        mergeSort(righthalf)

        # 记录左index
        i = 0
        # 记录右index
        j = 0
        # 记录排序列表的index
        k = 0
        # 比较两个有序列表,将较小的值插入alist
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
        # 处理左列表放入alist
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        # 处理右列表放入alist
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
    print('Merging', alist)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)

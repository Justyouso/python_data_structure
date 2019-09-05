# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-5 下午2:07


def sequentialSearch(alist, item):
    """
    功能:顺序查找
    实现:
        1. 从表中的第一个元素开始，依次与关键字比较。
        2. 若某个元素匹配关键字，则查找成功。
        3. 若查找到最后一个元素还未匹配关键字，则查找失败。
    :param alist: 列表
    :param item: 关键字
    :return: bool
    """
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
item = 30
print(sequentialSearch(alist, item))

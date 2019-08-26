# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-8-26 上午11:47


class MyNode:
    """
    功能:链表节点,以及节点相关操作
    """
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

#
# class UnorderedList:
#     def __init__(self):
#         self.head = None
#
#     # def isEmpty(self):
#     #     return self.head == None
#
#     def add(self, data):
#         """
#         功能:将一个数字加入链表
#         实现:创建节点(temp),temp.next->head,head->temp
#         :param data: 数据
#         :return:
#         """
#         temp = Node(data)
#         temp.setNext(self.head)
#         self.head = temp

if __name__ == '__main__':
    x = 1
    print(1)
    # unorderlist = UnorderedList()
    # unorderlist.add(1)
    # unorderlist.add(2)
    # unorderlist.add(3)
    # unorderlist.add(4)
    # unorderlist.add(5)
    # print(unorderlist)


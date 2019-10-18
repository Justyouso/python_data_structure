# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-10 下午4:11


class BinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def insert(self, key):
        """
        功能: 将key插入二叉树中
        实现: 将key添加到列表末尾,然后调用辅助函数(percUp)进行节点调整
        :param key: 插入的数
        :return: 
        """
        self.heaplist.append(key)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self, index):
        """
        功能: 自下向上交换节点,保证二叉树顺序
        :param index: 开始索引
        :return: 
        """
        while index // 2 > 0:
            if self.heaplist[index] < self.heaplist[index // 2]:
                self.heaplist[index], self.heaplist[index // 2] = self.heaplist[
                                                                      index // 2], \
                                                                  self.heaplist[
                                                                      index]
            else:
                break
            index = index // 2

    def delMin(self):
        """
        功能: 删除最小节点,删除后需要动态调整树节点
        实现: 
            1. 使用叶子节点赋值跟节点,删除叶子节点
            2. 找到当前节点的最小孩子节点
            3. 使用当前节点和最小孩子节点交换
        :return: 
        """
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize -= 1
        self.heaplist.pop()
        self.percUp(1)
        return retval

    def percDown(self, index):
        """
        功能: 自上向下交换节点
        :param index: 
        :return: 
        """
        while index * 2 <= self.currentSize:
            mc = self.minChild(index)
            if self.heaplist[index] > self.heaplist[mc]:
                self.heaplist[index], self.heaplist[mc] = self.heaplist[mc], \
                                                          self.heaplist[index]
            else:
                break
            index = mc

    def minChild(self, index):
        """
        功能: 找寻当前节点的最小孩子节点
        :param index: 
        :return: 
        """
        if index * 2 + 1 > self.currentSize:
            return index * 2
        else:
            if self.heaplist[index * 2] < self.heaplist[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1


    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heaplist = [0] + alist

        while i >0:
            self.percDown(i)
            i -=1
alist = [9,5,6,2,3]

binheap = BinHeap()
binheap.buildHeap(alist)


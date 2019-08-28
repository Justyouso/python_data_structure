# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-8-26 上午11:47


class Node:
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


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, data):
        """
        功能:将一个数字加入链表
        实现:创建节点(temp),temp.next->head,head->temp
        :param data: 数据
        :return:
        """
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        """
        功能:计算链表的大小
        实现:遍历链表,直到head==None
        :return: int
        """
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        """
        功能:查找数值(item)是否存在链表中
        实现:遍历链表,直到current==None和current.data=item
        :param item: 需要查找的数值
        :return: bool
        """
        current = self.head
        # 标识是否找到数值
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        """
        功能:查找数值item,并删除,只会删除一次数值,如: 1->2->2->3,删除后: 1->2->3
        实现:创建一个前节点指针previous,用于记录前节点,创建一个found标识符
            1.遍历链表,直到current==None和found==true(current.data=item)
            2.遍历链表会出现一下几种判断:
                1.current.data==item:找到指定数值,found=true
                2.current.data!=item:没找到指定数值,记录当前节点并继续循环下一个节点,previous=current,current=current.next
            3.找到数值才能更新(found=true),更新有两种情况:
                1.previous==None:表示第一个节点需要更改,即:head=current.next
                2.previous!=None:标识需要将previous(前节点)指向current.next(后节点),
                即:previous.next=current.next
        :param item: 需要删除的数值
        :return: bool
        """
        current = self.head
        # 前节点指针
        previous = None
        # 标识是否找到数值
        found = False
        # 判断item是否存在链表中
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        # 首先必须要找到才会执行链表更改操作
        if found:
            # head就是需要找到的值
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

        return found

    def remove_all(self, item):
        """
        功能:查找数值item,并删除,如: 1->2->2->3,删除后: 1->3
        实现:创建一个前节点指针previous,用于记录前节点,创建一个found标识符
            1.遍历链表,直到current==None,因为可能存在多个相同的节点，所以需要完整的遍历链表
            2.遍历链表会出现一下几种判断:
                1.current.data==item:找到指定数值,found=true
                2.current.data!=item:没找到指定数值,记录当前节点并继续循环下一个节点,
                found=false,previous=current,current=current.next
            3.找到数值才能更新(found=true),更新有两种情况:
                1.previous==None:表示第一个节点需要更改,且需将current指向head,方便继续
                遍历,即:head=current.next,current=head
                2.previous!=None:标识需要将previous(前节点)指向current.next(后节点),
                且需将current指向previous.next,即:previous.next=current.next,
                current=previous.next
        :param item: 需要删除的数值
        :return: 
        """
        current = self.head
        # 前节点指针
        previous = None
        # 标识是否找到数值
        found = False
        # 标识是否删除成功
        success = False
        # 判断item是否存在链表中
        while current != None:
            if current.getData() == item:
                found = True
                success = True
            else:
                # 需要删除多个相同的节点
                found = False
                previous = current
                current = current.getNext()
            # 首先必须要找到才会执行链表更改操作
            if found:
                # head就是需要找到的值
                if previous == None:
                    self.head = current.getNext()
                    # 将current->head,继续遍历查找是否有需要删除的节点
                    current = self.head
                else:
                    previous.setNext(current.getNext())
                    # 将current->previous.next,继续遍历查找是否有需要删除的节点
                    current = previous.getNext()

        return success


if __name__ == '__main__':
    unorderlist = UnorderedList()
    unorderlist.add(1)
    unorderlist.add(2)
    unorderlist.add(4)
    unorderlist.add(2)
    unorderlist.add(3)
    unorderlist.add(4)
    unorderlist.add(5)
    unorderlist.remove_all(2)
    unorderlist.remove(5)
    unorderlist.remove(3)
    print(unorderlist)

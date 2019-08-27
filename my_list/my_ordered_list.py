# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-8-27 下午2:24


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


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, data):
        """
        功能:将一个数字加入有序链表
        实现:创建一个前节点指针previous,用于记录前节点,创建一个found标识符,创建一个新节点(temp)
            1.遍历链表,直到current==None或found==true(current.data>item)
            2.遍历链表会出现一下几种判断:
                1.current.data<=item:找到指定数值,stop=true
                2.current.data>item:没找到指定数值,记录当前节点并继续循环下一个节点,
                previous=current,current=current.next
            3.更新有两种情况:
                1.previous==None:表示第一个节点需要更改,即:temp.next=head,
                head=current.next
                2.previous!=None:标识需要将previous(前节点)指向temp(新节点),
                新节点指向当current(前节点),即:previous.next=current.next
        :param data: 数据
        :return:
        """
        current = self.head
        # 新节点
        temp = Node(data)
        # 标识是否停止循环
        stop = False
        # 前节点指针
        previous = None
        while current != None and not stop:
            if data <= current.getData():
                stop = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            previous.setNext(temp)
            temp.setNext(current)

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
        实现:遍历链表,直到current==None或current.data>=item
        :param item: 需要查找的数值
        :return: bool
        """
        current = self.head
        # 标识是否找到数值
        found = False
        # 标识是否停止循环
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        """
        功能:查找数值item,并删除,只会删除一次数值,如: 1->2->2->3,删除后: 1->2->3
        实现:创建一个前节点指针previous,用于记录前节点,创建一个found标识符表示找到数值,创建
            一个stop标识符表示是否停止循环(当item>current.data时需要停止循环)
            1.遍历链表,直到current==None或found==true(current.data==item)或stop==true
            (current.data<item)
            2.遍历链表会出现一下几种判断:
                1.current.data==item:找到指定数值,found=true
                2.current.data>item:当前节点数值>item,stop=true
                3.current.data<item:没找到指定数值,记录当前节点并继续循环下一个节点,previous=current,current=current.next
            3.找到数值并且没有停止循环才能更新(found==true and stop==false),更新有两种情况:
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
        # 标识是否停止循环
        stop = False
        # 判断item是否存在链表中
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        # 首先必须要找到且没有停止循环才会执行链表更改操作
        if found and not stop:
            # head就是需要找到的值
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

        return found

    def remove_all(self, item):
        """
        功能:查找数值item,并删除,如: 1->2->2->3,删除后: 1->3
        实现:创建一个前节点指针previous,用于记录前节点,创建一个found标识符表示找到数值,创建
            一个stop标识符表示是否停止循环(当item>current.data时需要停止循环)
            1.遍历链表,直到current==None或found==true(current.data==item)或stop==true
            (current.data<item)
            2.遍历链表会出现一下几种判断:
                1.current.data==item:找到指定数值,found=true
                2.current.data>item:当前节点数值大于item,stop=true
                3.current.data<item:没找到指定数值,记录当前节点并继续循环下一个节点,
                found=false,previous=current,current=current.next
            3.找到数值并且没有停止循环才能更新(found==true and stop==false),更新有两种情况:
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
        # 标识是否停止循环
        stop = False
        # 判断item是否存在链表中
        while current != None and not stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                # 需要删除多个相同的节点
                found = False
                previous = current
                current = current.getNext()
            # 首先必须要找到且没有停止循环才会执行链表更改操作
            if found and not stop:
                # head就是需要找到的值
                if previous == None:
                    self.head = current.getNext()
                    # 将current->head,继续遍历查找是否有需要删除的节点
                    current = self.head
                else:
                    previous.setNext(current.getNext())
                    # 将current->previous.next,继续遍历查找是否有需要删除的节点
                    current = previous.getNext()

        return found


if __name__ == '__main__':
    orderlist = OrderedList()
    orderlist.add(1)
    orderlist.add(2)
    orderlist.add(4)
    orderlist.add(2)
    orderlist.add(3)
    orderlist.add(4)
    orderlist.add(5)
    orderlist.add(0)
    orderlist.add(6)
    orderlist.search(5)
    orderlist.remove_all(2)
    orderlist.remove(5)
    orderlist.remove(3)
    print(orderlist)

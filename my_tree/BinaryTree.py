# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-9 下午3:17


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newnode):
        if not isinstance(newnode, BinaryTree):
            newnode = BinaryTree(newnode)

        newnode.leftChild = self.leftChild
        self.leftChild = newnode

    def insertRight(self, newnode):
        if not isinstance(newnode, BinaryTree):
            newnode = BinaryTree(newnode)

        newnode.rightChild = self.rightChild
        self.rightChild = newnode

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
        print(self.key)

    def inorder(self):
        if self.leftChild:
            self.leftChild.preorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.preorder()


r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
# r.getRightChild().setRootVal('hello')
# print(r.getRightChild().getRootVal())


print("前序")
r.preorder()
print("中序")
r.inorder()
print("后序")
r.postorder()

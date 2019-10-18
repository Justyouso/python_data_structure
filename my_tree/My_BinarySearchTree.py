# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-11 下午5:26


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rigthChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, value, lc, rc):
        """
        功能: 替换根节点值
        实现: 将跟节点的孩子节点辅助给根节点,接着将跟节点的孩子节点的孩子节点指向根节点,
        :param key: 跟节点的孩子节点key
        :param value: 跟节点的孩子节点value
        :param lc: 根节点的孩子节点的左孩子
        :param rc: 跟节点的孩子节点的右孩子
        :return: 
        """
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        """
        功能: 删除功能查找后继节点
        实现: 1. 如果节点有右子节点,则后继节点是右子树中的最小的键。
             2. 如果节点没有右子节点并且是父节点的左子节点,则父节点是后继节点。
             3. 如果节点是其父节点的右子节点,并且它本身没有右子节点,则此节点的后继节点是其父节
             点的后继节点,不包括此节点。
        :return: 
        """
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rigthChild = None
                    succ = self.parent.findMin()
                    self.parent.rigthChild = self
        return succ

    def findMin(self):
        """
        功能: 查找当前节点最小值
        实现: 在查找树中,最小值节点试试树的最左节点
        :return: 
        """
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        """
        功能: 
        :return: 
        """
        if self.isLeaf():
            if self.isLeftChild():
                self.leftChild = None
            else:
                self.rightChild = None
        elif self.hasAnyChildren():
            # 当前节点有左孩子
            if self.hasLeftChild():
                # 当前节点是左节点
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            # 当前节点有右孩子
            else:
                # 当前节点是左节点
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __contains__(self, item):
        return True if self._get(item, self.root) else False

    def __delete__(self, item):
        self.delete(item)

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            return res.payload if res else None
        else:
            return None

    def get_node(self, key):
        if self.root:
            res = self._get(key, self.root)
            return res if res else None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif key == currentNode.key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rigthChild)

    def _put(self, key, val, currentNode):
        """
        功能: 遍历比较key,选择合适的地方插入数据
        :param key: 
        :param val: 
        :param currentNode: 
        :return: 
        """
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, ket not in tree')

    def remove(self, currentNode):
        # 当前结点没有孩子结点
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        # 当前节点存在两个孩子节点
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        # 当前结点存在一个孩子结点
        else:
            # 当前存在左孩子
            if currentNode.hasLeftChild():
                # 当前结点是父节点的左孩子
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                # 当前结点是父节点的右孩子
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.repalceNodedata(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)

            # 当前结点存在右孩子
            else:
                # 当前结点是父节点的左孩子
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                # 当前节点是父节点的右孩子
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.repalceNodedata(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)


mytree = BinarySearchTree()
mytree[17] = 17
mytree[5] = 5
mytree[2] = 2
mytree[11] = 11
mytree[9] = 9
mytree[7] = 7
mytree[8] = 8
mytree[16] = 16
mytree[35] = 35
mytree[29] = 29
mytree[38] = 38

x = mytree.get_node(17)
for i in iter(x):
    print(i)
# mytree.remove(x)

print(mytree.__iter__().payload)



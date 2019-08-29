# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-8-29 下午2:04


class HashTable:
    def __init__(self):
        self.size = 3
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunc(self, value):
        """
        功能:计算hash值
        实现:简单除余
        :param value: 需要计算hash的值
        :return: int
        """
        return value % self.size

    def rehash(self, oldhash):
        """
        功能:为防止冲突进行rehash
        实现:将oldhash+1,再与size求余
        :param oldhash: 原有hash值
        :return: int
        """
        return (oldhash + 1) % self.size

    def put(self, key, value):
        """
        功能:添加key,value到哈希表中
        实现:将key放入插槽列表,value放入数据列表
            1.获取key的hash值,hashvalue=hashfunc(key)
            2.若hashvalue在插槽列表中无值,则给slot和data列表赋值
            3.若hashvalue在插槽列表中有值,有两种情况
                1.slots[hashvalue]==key:更新data[hashvalue]即可
                2.slots[hashvalue]!=key:将hashvalue往后移动(nextslot=rehash),
                直到slots[nextslot]==None或slots[nextslot]==key
                3.判断nextslot在slots中是否存在值,若无,则给slot和data赋值,若有,
                更新data[nextslot]即可
        :param key: 字典key
        :param value: 字典value
        :return: 
        """
        # 计算hash值
        hashvalue = self.hashfunc(key)
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = value
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = value
            else:
                # 进行rehash
                nextslot = self.rehash(hashvalue)
                while self.slots[nextslot] is not None and self.slots[
                    nextslot] != key and nextslot != hashvalue:
                    nextslot = self.rehash(nextslot)
                try:
                    if nextslot == hashvalue:
                        raise Exception(
                            "error: slot len is {}".format(self.size))
                    if self.slots[nextslot] is None:
                        self.slots[nextslot] = key
                        self.data[nextslot] = value
                    else:
                        self.data[nextslot] = value
                except Exception as ex:
                    print(ex)

    def get(self, key):
        """
        功能:查询key的value值
        实现:计算hashvalue,若slots[hashvalue]==key,直接取值,否则,进行rehash,并比较key值,
        直到slot[nexthash]==key或者nexthash==hashvalue
        :param key: 字典key
        :return: 
        """
        hashvalue = self.hashfunc(key)
        data = None
        stop = False
        if self.slots[hashvalue] == key:
            data = self.data[hashvalue]
        else:
            nexthash = self.rehash(key)
            while self.slots[nexthash] != key and not stop:
                if nexthash == hashvalue:
                    stop = True
                nexthash = self.rehash(nexthash)
            if not stop:
                data = self.data[nexthash]

        return data

    def __setitem__(self, key, value):
        return self.put(key,value)

    def __getitem__(self, key):
        return self.get(key)

if __name__ == '__main__':
    hashtable = HashTable()
    hashtable.put(1, 1)
    hashtable.put(2, 2)
    hashtable.put(4, 4)
    hashtable[1]=3
    y = hashtable[1]
    x = hashtable.get(2)
    print(x)

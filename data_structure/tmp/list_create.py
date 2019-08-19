# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-8-16 上午11:29

def list1():
    l = []
    for i in range(10000):
        l = l + [i]


def list2():
    l = []
    for i in range(10000):
        l.append(i)


def list3():
    l = [i for i in range(10000)]


def list4():
    l = list(range(10000))



from timeit import Timer

t1 = Timer("list1()", "from __main__ import list1")
print("concat", t1.timeit(number=100), "milliseconds")
t2 = Timer("list2()", "from __main__ import list2")
print("append", t2.timeit(number=100), "milliseconds")
t3 = Timer("list3()", "from __main__ import list3")
print("comprehension", t3.timeit(number=100), "milliseconds")
t4 = Timer("list4()", "from __main__ import list4")
print("list range", t4.timeit(number=100), "milliseconds")
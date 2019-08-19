# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-8-19 下午10:08

from pythonds.basic.stack import Stack


def parChecker(symbolString):
    """
    功能：检查括号字符串是否平衡,如:'(()())'是平衡字符串,'()(('是非平衡字符串
    实现：使'('为开始符号,当为'('压入栈,否则出栈
    :param symbolString: 字符串
    :return: bool
    """
    s = Stack()
    balanced = True
    index = 0
    while len(symbolString) > index and balanced:
        if symbolString[index] == '(':
            s.push(symbolString[index])
        else:
            # 只要进入循环体栈就不可能为空,除非该字符串不是平衡的
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
    # 只有在栈必须为空时才能是平衡字符串
    if balanced and s.isEmpty():
        return True
    else:
        return False


symbolString = '((())())'
parc = parChecker(symbolString)
print(parc)

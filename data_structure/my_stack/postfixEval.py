# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-8-21 下午7:26

from pythonds.basic.stack import Stack


def postfixEval(postfixExpr):
    """
    功能： 后缀表达式求值,如:1-2*3=-5
    实现： 遍历后缀表达式,会出现如下几种状况:
        1. 操作数: 压入栈stack
        2. 运算符: fnum=stack.pop,snum=stack.pop,result=snum '运算符' fnum,再将result入栈
    :param postfixExpr: 后缀表达式字符串
    :return: int
    """
    stack = Stack()
    tokenlist = postfixExpr.split()
    for token in tokenlist:
        if token in '0123456789':
            stack.push(int(token))
        else:
            fnum = stack.pop()
            snum = stack.pop()
            result = doMath(snum, fnum, token)
            stack.push(result)
    return stack.pop()


def doMath(snum, fnum, operator):
    """
    功能： 求值
    :param snum: 数值2
    :param fnum: 数值1
    :param operator: 运算符
    :return: int
    """
    if operator == '+':
        return snum + fnum
    if operator == '-':
        return snum - fnum
    if operator == '*':
        return snum * fnum
    if operator == '/':
        return snum / fnum

print(postfixEval('1 2 3 - +'))
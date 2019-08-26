# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-8-20 下午10:06

from pythonds.basic.stack import Stack


def infixToPostfix(infixexpr):
    """
    功能： 将中缀表示法转换成后缀表示法,如(A+B)*C->AB+C*,A+B*C->ABC*+
    实现： 
        1.对运算符进行分级,'+,-':2级,'*,/':3级,'(':1级,'('需要进行特殊处理
        2.创建需要的变量:result=列表,stack=栈
        2.遍历字符串,对字符的操作有不同的区别,result:列表,stack:栈:
            2.1.运算数字(A,B,1,2):append到result
            2.2.运算符'(': push到stack
            2.3.运算符')': stack.pop 并将结果append到result,直到出现运算符'('
            2.4.运算符(+,-,*,/):将运算符token和toptoken=stack.peek进行比较优先级,
                2.4.1.若toptoken>=token,则stack.pop并将结果append到result,直到toptoken<token
                2.4.2.若toptoken<token,则push到stack
    :param infixexpr: 字符串表达式
    :return: str
    """
    stack = Stack()
    prec = {'+': 2, '-': 2, '*': 3, '/': 3, '(': 1}
    tokenlist = infixexpr.split()
    result = []

    for token in tokenlist:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            result.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            topToken = stack.pop()
            while topToken != '(':
                result.append(topToken)
                topToken = stack.pop()
        else:
            while (not stack.isEmpty()) and (prec[stack.peek()] >= prec[token]):
                topToken = stack.pop()
                result.append(topToken)
            stack.push(token)

    while not stack.isEmpty():
        result.append(stack.pop())
    return ''.join(result)


print(infixToPostfix("( A + B ) * ( C + D )"))
print(infixToPostfix("A * B + C * D "))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

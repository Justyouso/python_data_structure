# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-6 上午10:52


def moveTower(height, fromPole, topPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, topPole)
        moveDisk(fromPole, topPole)
        moveTower(height - 1, withPole, topPole, fromPole)


def moveDisk(fp, tp):
    print('move disk from', fp, 'to', tp)


moveTower(4, 'A', 'C', 'B')

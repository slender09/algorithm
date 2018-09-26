# -*- coding: utf-8 -*-

# 成绩排名

__author__ = "slender"

score = []
n = int(input())
if n >=0:
    for i in range(n):
        in_sc = [x for x in input().split()]
        score.append(in_sc)
    score.sort(key=lambda x: int(x[2]))
    
    print(*score[-1][0:-1])
    print(*score[0][0:-1])
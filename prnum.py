# -*- coding: utf-8 -*-

# 素数对猜想

__author__ = "slender"

from math import sqrt

ls = []
num = 0
n = int(input())

for i in range(2, n+1):
    for k in range(2, int(sqrt(i))+1):
        if i % k == 0:
            break
    else:
        ls.append(i)
        if len(ls)>1 and ls[-1]-ls[-2] == 2:
            num += 1

print(num)
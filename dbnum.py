# -*- coding: utf-8 -*-

# 数组移动

__author__ = "slender"


n = int(input())
if len(str(n))<=20:
    if set([int(i) for i in str(n)]) == set([int(i) for i in str(2*n)]) and len(str(n)) == len(str(2*n)):
        print('Yes')
        print(2*n)
    else:
        print('No')
        print(2*n)
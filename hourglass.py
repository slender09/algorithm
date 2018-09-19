# -*- coding: utf-8 -*-

# 打印沙漏

__author__ = "slender"

from math import sqrt
in_s = input()
num = int(in_s.split()[0])
pic = in_s.split()[1]
n = int(sqrt(((num+1)/2)))
if num ==0:
    print()
    print(num)
else:
    for i in range(n,0,-1):
        print(' '*(n-i)+pic*(2*i-1))
    for i in range(2,n+1,1):
        print(' '*(n-i)+pic*(2*i-1))
    print(num-2*n**2+1)


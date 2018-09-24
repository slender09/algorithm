# -*- coding: utf-8 -*-

# 数组移动

__author__ = "slender"


N, M=[int(i) for i in input().split()]
num_ls=list(input().split())
while True:
    if len(num_ls) != N:
        num_ls=list(input().split())
    else:
        break
if N>=1 and N<=100 and M>=0:
    if M>=N and M%N==0:
        print(' '.join(num_ls))
    elif M%N<=N//2:
        for i in range(0,M%N):
            num_ls.insert(0,num_ls[-1])
            del num_ls[-1]
        print(' '.join(num_ls))
    else:
        for i in range(0,N-M%N):
            num_ls.append(num_ls[0])
            del num_ls[0]
        print(' '.join(num_ls))
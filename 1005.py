# -*- coding: utf-8 -*-

# 继续(3n+1)猜想

__author__ = "slender"

# -*- coding: utf-8 -*-

n = int(input())

a = list(map(int,input().split()))

b = []

for i in range(n):
    e = a[i]
    s = str(a[i])
    while e != 1:
        if e % 2 == 0:
            e = int(e / 2)
            s += str(e)
        else:
            e = int((3*e+1)/2)
            s += str(e)
    b.append(s)
d = []
for i in range(n):
    for k in b:
        if (b[i] in k) and (b[i]!=k):
            flag = 0
            break
        else:
            flag = 1
    if flag == 1:
        d.append(a[i])
d.sort(reverse=True)
print(*d)
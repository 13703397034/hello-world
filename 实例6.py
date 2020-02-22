#coding: utf-8
ls = []
for i in range(1,4):
    x = int(input())
    ls.append(x)
ls.sort()
for i in ls:
    print(i,end=' ')
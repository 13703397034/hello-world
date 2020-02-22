#coding: utf-8
#分解最小质因数
num = int(input("请输入您要分解的数："))
l = [i for i in range(2,num+1)]
ls = []
for j in l:
    while num != j:
         if num%j==0:
           num=num//j
           ls.append(j)
    break
ls.append(num)
for i in ls:
    print(i,end=" ")



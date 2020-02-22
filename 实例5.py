#coding: utf-8

m = input("请输入第一个数：")
n = input("请输入第二个数：")
o = input("请输入第三个数：")

def panduan(a,b,c):
    i = 0
    if a > b:
        i = b
        b = a
        a = i
    if a > c:
        i = c
        c = a
        a = i
    if b > c:
        i = c
        c = b
        b = i
    print(a , b , c)
panduan(m,n,o)






#coding: utf-8
#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
import  math

for i in range(1,10001):
    m=int(math.sqrt(i+100))
    n=int(math.sqrt(m+268))
    if (n*n== m+268) and (m*m == i+100 ):
        print(i)




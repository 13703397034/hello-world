#coding: utf-8
#判断101--200间的所有素数
import math
def sushu():
    num = 0
    for i in range(101,201):
        if i%2==0 and int(math.sqrt(i))*int(math.sqrt(i))==i:
            print(i,end=" ")
            num+=1

    print("一共{0}个素数".format(num))
sushu()


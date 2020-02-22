#coding: utf-8
import random
n = input("请输入您要出的题目类型代码（例如：1、加法 2、减法）：")
cishu = int(input("请输入要生成的个数："))
w = int(n)

if w == 1:

    for i in range(1,cishu+1):
        num1 = int(random.uniform(1,10))
        num2 = int(random.uniform(1,10))
        print("{0}+{1}=".format(num1,num2),end="           ")
        if i%5==0:
            print()





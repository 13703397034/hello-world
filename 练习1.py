# -*- coding: UTF-8 -*-
#题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
#1.程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去
#　　　　　　掉不满足条件的排列。
ls = int(input("请输入您要判断数字:"))
def 实例1(ls):

    m = 0
    for i in range(1,ls):

        for j in range(1,ls):
            for k in range(1,ls):
                if i == j or i ==k or j==k:
                    continue
                else:
                    n = i*100+j*10+k
                    m=m+1
                    print("数值是{0}".format(n))

    print("一共有{0}个数".format(m))
实例1(ls)
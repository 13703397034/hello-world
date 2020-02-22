#coding: utf-8
yer = int(input("请输入年份："))
mon = int(input("请输入月份："))
day = int(input("请输入天数："))
month = [0,31,59,90,120,151,181,212,243,273,304,334]
num = day + month[mon-1]
def run(yer,num):
    if (yer%4 ==0 and yer%100!=0) or yer%400 == 0:
        num = num+1
        print("闰年的第{0}天".format(num))
    else:
        print("今年的第{0}天".format(num))
run(yer , num)

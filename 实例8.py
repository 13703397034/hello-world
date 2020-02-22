#coding: utf-8
#斐波烈契数
def fun (n):
    if n == 1 :
        return 1
    if n == 2 :
        return 1

    return fun(n-1)+fun(n-2)

print(fun(8))

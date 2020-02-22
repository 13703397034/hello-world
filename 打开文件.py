#coding: utf-8
with open('C:\\Users\\zhoubo\\Desktop\\new.txt') as file_object:
    str = file_object.read()
    print(str.rstrip())
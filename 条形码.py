#coding: utf-8
from pystrich.code39 import Code39Encoder

ls = ['1234251','1273291','2367292','198321']

def sbarcode(name):
#生成条形码
     encoder = Code39Encoder(name)
     named = name
     encoder.save("c:\\new\\"+named+".jpg")
for i in ls:
    sbarcode(i)
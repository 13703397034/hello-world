#coding: utf-8
import xlrd
from pystrich.code39 import Code39Encoder

def sbarcode(name):
#生成条形码代码
     encoder = Code39Encoder(name)
     named = name
     encoder.save("c:\\new\\"+named+".jpg")
def excle():
    #操作excle表并把第一列的单元格
    workbook = xlrd.open_workbook('C:\\注册模板.xls')
    sheets = workbook.sheet_names()
    #print("抓取的sheet名称是:{0}".format(sheets))
    sheet1 = workbook.sheet_by_name('注册模板')
    num_rows = sheet1.nrows
    ls=[]
    for i in range(1,num_rows):
        cell=sheet1.cell_value(i, 0)
        ls.append(cell)
    return ls
vol = excle()
for i in vol:
    sbarcode(i)


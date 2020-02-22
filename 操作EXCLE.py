#coding: utf-8
import xlrd

workbook = xlrd.open_workbook('C:\\Users\zhoubo\Desktop\注册模板.xls')
sheets = workbook.sheet_names()
#print("抓取的sheet名称是:{0}".format(sheets))
sheet1 = workbook.sheet_by_name('注册模板')
num_rows = sheet1.nrows

ls1=[]
for i in range(1,num_rows):
    cell = []
    for j in range(0,18):

        cell.append(sheet1.cell_value(i, j))
    ls1.append(cell)

for i in ls1:
    for j in i:
        print(str())


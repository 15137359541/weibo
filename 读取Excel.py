#coding=utf8
# 导入xlrd模块
import xlrd
from xlutils.copy import copy
#设置文件名和路径
fname = 'd:/TestData.xlsx'
# 打开文件
filename = xlrd.open_workbook(fname)
#获取当前文档的表(得到的是sheet的个数，一个整数）
sheets=filename.nsheets



#获取sheet对象，方法有3种：
# 第一种:#通过sheet名字来获取，当然如果你知道sheet名字了可以直接指定
# 得到的是一个列表集合[u'etsy_sheet']
sheet_list = filename.sheet_names()
#获取指定的sheet名的表,sheet结果：(<xlrd.sheet.Sheet object at 0x027FC890>)
# 找不到报错：xlrd.biffh.XLRDError: No sheet named <'etsy_sheet1'>
# sheet=filename.sheet_by_name(sheet_list[0])

#第二种
# sheet=filename.sheet_by_index(0)     #通过sheet索引获得sheet对象
# 第三种：
sheet = filename.sheets()[0] #通过sheet索引获得sheet对象
# print sheet
#获取行数
nrows = sheet.nrows
# 获取列数
ncols = sheet.ncols
#获取第一行,第一列数据数据
cell_value = sheet.cell_value(1,1)
'''
###除了cell值内容外还有附加属性，如：
'likai:输出text:"likai"  或者
2018-1-25 13:44:49输出xldate:43125.57278935185

'''
###除了cell值内容外还有附加属性，如：text:"likai"后者2018-1-25 13:44:49输出xldate:43125.57278935185
cell_value1 = sheet.cell(3,0)
print cell_value1

#获取第一行数据
row_data = sheet.row_values(1)
#获取第一列,第四行一下的数据
col_data = sheet.col_values(0,4)
#获取各行数据
row_list=[]
for i in range(0,nrows):
    row_datas = sheet.row_values(i)
    row_list.append(row_datas)
# print row_list

#文件copy
wb = copy(filename)#<xlwt.Workbook.Workbook object at 0x025EE1F0>
new_sheet = wb.get_sheet(0)#<xlwt.Worksheet.Worksheet object at 0x027F3EB0>
new_sheet.write(3,3,"new wenjian")
wb.save("d:/TestData1.xlsx")

#coding=utf8
import csv
import pandas as pd
'''
#文件头，一般是数据名
fileHeader = ["name","score",'age']
#下面是两行数据
data1=['wang',80,20]
data2=['li',90,21]
#创建文件名，打开文件(可以自动创建文件名）
csvFile = open('d:/testData1.csv','w')#<open file 'd:/testData.csv', mode 'w' at 0x0044D1D8>
#创建字典csv对象
writer = csv.DictWriter(csvFile,fileHeader)#<_csv.writer object at 0x027440F0>
#添加表头
writer.writeheader()
# 添加表头
# 但是如果此时直接写入内容，会导致没有数据名，所以，应先写数据名（也就是我们上面定义的文件头）。
# 写数据名，可以自己写如下代码完成：
# writer.writerow(dict(zip(fileheader, fileheader)))
#写入数据
writer.writerow({'name':'likai',"score":"99","age":"10"})
#关闭文件
csvFile.close()
print csvFile
print writer
'''
#任意多种列表数据
a = ["likai",'wangfeng','xiaoyu','dalian']
b =[20,23,20,10]
#写入的时候是以列写的key代表列名，value代表数值
dataframe = pd.DataFrame({"name":a,"age":b})
#将DataFram存储为csv，index表示是否显示行名，default=True
dataframe.to_csv('d:/pandasData.csv',index=False,sep=',')


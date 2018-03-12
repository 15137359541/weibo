#coding=utf8
import csv
'''
csvFile = open("d:/testData1.csv", "r")
dict_reader = csv.DictReader(csvFile)
#输出属性名，为列表
print(dict_reader.fieldnames)
#输出字典形式的数据
for row in dict_reader:
    print(row)
'''
import pandas as pd
data = pd.read_csv('d:/pandasData.csv')
print data

dframe = pd.DataFrame.from_csv('d:/pandasData.csv')
print dframe
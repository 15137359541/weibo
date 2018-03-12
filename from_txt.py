import xlwt
filed = []
all_good_id={}
error_list=[]
with open('con_es2.txt','r',encoding="UTF-8") as f:

    for i in range(7620):
        lines = f.readline()
        for i in lines.split(","):
            try:
                con = i.split(":",1)[1]
                filed.append(con)
            except:
                error_list.append(lines)

        filed.append(1)
        goodId = filed[0]
        goodNum = filed[-1]
        if goodId in all_good_id:
            all_good_id[goodId][-1] = all_good_id.get(goodId)[-1] + 1

        else:
            all_good_id[goodId] = filed
        filed = []

print(all_good_id)
#创建一个Excel表格
wbk = xlwt.Workbook(encoding="utf-8",style_compression=0)
#为表格添加一个工作表
sheet = wbk.add_sheet("items",cell_overwrite_ok=True)
#表头
fileHeader=['good_id',"good_url","pic","title","price","reviews","favorited",'shop_name',"shop_url","descriptions","total"]
for i in range(len(fileHeader)):
    sheet.write(0,i,fileHeader[i])
#添加内容
kinds=0
for num,con in all_good_id.items():
    kinds +=1
    for item in range(len(con)):

        sheet.write(kinds,item,con[item])


print(error_list)
wbk.save('Data.xlsx')





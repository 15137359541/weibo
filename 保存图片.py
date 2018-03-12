from GetPost import gets

url="https://cbu01.alicdn.com/img/ibank/2017/051/369/6016963150_1713371864.jpg"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
#
# # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
# content =gets(url, params = tp, headers = headers)
#
# # 查看响应内容，response.text 返回的是Unicode格式的数据
# print (content["message"])
# with open("aaa.jpg",'w')as f:
#     f.write(content["message"])
import requests
from PIL import Image
from io import BytesIO

response = requests.get(url=url,headers=headers)
image = Image.open(BytesIO(response.content))
image.save('5.jpg')

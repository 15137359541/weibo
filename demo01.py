#coding=utf8
import requests
from urllib.parse import urlencode


#将cookies转换成字典形式，zhihu_cookie为保存的cookie文件，跟程序处在同一路径
def get_cookie():
    with open('cookies.txt','r') as f:
        cookies={}
        for line in f.read().split(';'):
            print (line)
            name,value=line.strip().split('=',1)  #1代表只分割一次
            cookies[name]=value
        return cookies


if __name__=="__main__":
    headers = {
        'Host': 'www.etsy.com',
        'Referer': 'https://www.etsy.com/shop/VeryCharms/reviews',
        'upgrade-insecure-requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    parame1 = {"ref": "pagination", "page": str(47)}

    res_cookies= get_cookie()
    print (res_cookies)
    print("++++++++++++++++++")
    base_url_ = 'https://www.etsy.com/shop/VeryCharms/reviews?'
    url = base_url_ + urlencode(parame1)
    print (url)
    print("$$$$$$$$$$$$$$$$$$")

    response=requests.get(url=url,headers=headers,cookies=res_cookies)
    print (response.cookies)
    print('___________')
    html=response.content.decode("utf-8")
    ccon=html.replace('\n', '').replace('\r', '').replace('\t', '')
    print (ccon)
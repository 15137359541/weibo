# coding=utf-8
"""
不加图片
"""
import re,time,requests
# from GetPost import gets,posts
from urllib.parse import urlencode
num=1
all_good_id={}

def get_cookie():
    with open('cookies_likai.txt','r') as f:
        my_cookies={}
        for line in f.read().split(';'):
            print (line)
            name,value=line.strip().split('=',1)  #1代表只分割一次
            my_cookies[name]=value
        return my_cookies

def getFeedback(base_url,res_cookies):
    global num
    for page in range(1,1500):
        time.sleep(1)
        parame1 = {"ref": "pagination", "page": str(page)}
        url = base_url + urlencode(parame1)
        print("第%s页内容"% page)
        print (url)
        try:
            response=requests.get(url=url,headers=headers,cookies=res_cookies,timeout=10)
            if response:
                html =response.content.decode("utf-8").replace('\n', '').replace('\r', '').replace('\t', '')
                # print html
                # print ("_____________________")
                #需要多每一个评论总体做处理
                feedbacks=  re.findall(' <div class="flag-body pb-xs-0">(.*?)show-xs',html)
                for feedback in feedbacks:
                    print("第%s条评论"% num)
                    try:
                        num += 1
                        #评论时间
                        # feedbacktime=feedBackTime(feedback)
                        #评论图片和题目
                        feedbackTitle,goodurl=feedbackPictureTitle(feedback)
                        print (goodurl)
                        # 商品id编号
                        goodId = re.search('(\d+)', goodurl).group(1).strip()
                    except:
                        feedbackTitle = "no value title"
                        goodurl = "no available url"
                        goodId = 000000

                    # 写入文件
                    with open("con_es1.txt", "a")as f:
                        f.write("Id:%s"% goodId)
                        f.write("标题：%s  " % feedbackTitle)
                        f.write("商品url %s" % goodurl)
                        f.write("\n")

                    # 去除重复
                    if goodId in all_good_id:
                        all_good_id[goodId] = all_good_id.get(goodId) + 1

                    else:
                        all_good_id[goodId] = 1
                        with open("con_es2.txt", "a")as f:
                            f.write("Id:%s" % goodId)
                            f.write("标题：%s  " % feedbackTitle)
                            f.write("商品url %s" % goodurl)
                            f.write("\n")
            else:
                return "没有数据"
        except:
            print('Error,no response')


    return all_good_id



#对评论的图片和标题做处理
def feedbackPictureTitle(feedback):
    pictureTitle=re.search('<div class="flag-img">                <a href="(.*?)" title="(.*?)" class(.*?)<div class="card-img-wrap">                        <img src="(.*?)"',feedback)
    if pictureTitle:
        # 商品url
        goodurl=pictureTitle.group(1).strip()
        feedbackTitle=pictureTitle.group(2).strip()
        return feedbackTitle,goodurl
    else:
        return 'no title',"no goodurl"



import json
if __name__=="__main__":
    url='https://www.etsy.com/shop/CreatingUnkamen/reviews?'
    headers = {
        'Host': 'www.etsy.com',
        'Referer': 'https://www.etsy.com/shop/VeryCharms/reviews',
        'upgrade-insecure-requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }

    res_cookies= get_cookie()


    res = getFeedback(url,res_cookies)
    res_n=sorted(res.items(),key=lambda item:item[1],reverse=True)
    print (res_n)
        # 写入文件
    with open("con_es3.txt", "a")as f:
        json.dump(res_n, f)
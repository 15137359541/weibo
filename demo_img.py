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
    with open('cookies.txt','r') as f:
        my_cookies={}
        for line in f.read().split(';'):
            print (line)
            name,value=line.strip().split('=',1)  #1代表只分割一次
            my_cookies[name]=value
        return my_cookies
def get_cookie1():
    with open('cookie1.txt','r') as f:
        my_cookies1={}
        for line in f.read().split(';'):
            print (line)
            name,value=line.strip().split('=',1)  #1代表只分割一次
            my_cookies1[name]=value
        return my_cookies1

def getFeedback(base_url,res_cookies):
    global num
    for page in range(1,200):
        time.sleep(1)
        parame1 = {"ref": "pagination", "page": str(page)}
        url = base_url + urlencode(parame1)
        print("第%s页内容"% page)
        print (url)
        try:
            response=requests.get(url=url,headers=headers,cookies=res_cookies,timeout=30)
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
                        goods_list(goodurl)
                        # 商品id编号
                        goodId = re.search('(\d+)', goodurl).group(1).strip()
                    except:
                        feedbackTitle = "no value title"
                        goodurl = "no available url"
                        goodId = 000000

                    # 写入文件
                    with open("con_es1.txt", "a")as f:
                        f.write("Id:%s,"% goodId)
                        f.write("title:%s," % feedbackTitle)
                        f.write("good_url:%s " % goodurl)
                        f.write("\n")
            else:
                return "没有数据"
        except:
            print('Error,no response')


    return 'over'

#商品详情页
def goods_list(url):

    response = requests.get(url=url, cookies=res_cookies1, timeout=30)
    if response:
        # 商品id编号
        goodId = re.search('(\d+)', url).group(1).strip()
        # 简单处理详情页面
        html = response.content.decode("utf-8").replace('\n', '').replace('\r', '').replace('\t', '')
        #图片
        img_url = re.search('data-full-image-href="(.*?)"', html)
        # print('图片地址:',img_url.group(1))
        if img_url:
            img_url=img_url.group(1)
        else:
            img_url="no img_url"
        #标题
        title=re.search('<span itemprop="name">(.*?)</span>',html)
        if title:
            title=title.group(1).replace(",",";")
        else:
            title='no title'
        # 价格,第一种情况，拥有现价，原价
        try:
            price=re.search('<span id="listing-price" class="vertical-align-middle ">        <span>(.*?)</span>        <strike class="text-gray-lighter text-smallest normal">(.*?)</strike>',html)

            price_now=price.group(1).strip()

        #价格，第二种情况，没有原价，只有现价
        except:
            try:
                price = re.search(
                    '<span id="listing-price" class="vertical-align-middle ">(.*?)<meta itemprop="currency" content="USD"/>',
                    html)
                price_now=price.group(1).strip()

            except:
                price_now=0


        #评论和喜欢的人
        feedback_loved=re.search('<a href="#reviews">(.*?) reviews</a>(.*?)Favorited by: <a href="(.*?)">(.*?) people</a>', html)
        if feedback_loved:
            feedback=float((feedback_loved.group(1)))
            favorited=float(feedback_loved.group(4))
        else:
            feedback,favorited="no feedback",'no favorited'

        #店铺名和店铺url；
        shopNameUrl=re.search('<a itemprop="url" href="(.*?)"><span itemprop="title">(.*?)</span></a>',html)
        #店铺名有两种匹配规则
        if shopNameUrl:
            #商电名
            shop_name=shopNameUrl.group(2)
            #商电url:
            shop_url=shopNameUrl.group(1)
        else:
            shopNameUrl = re.search('<a class="text-gray-darker" itemprop="url" href="(.*?)"><span itemprop="title">(.*?)</span></a>', html)
            if shopNameUrl:
                # 商电名
                shop_name = shopNameUrl.group(2)
                # 商电url:
                shop_url = shopNameUrl.group(1)
            else:
                shop_name,shop_url='no shop',''
        #描述
        Descriptions = re.search('<div class=" text-gray prose">        <div>(.*?)</div>', html)
        if Descriptions:
            descriptions=Descriptions.group(1).strip().replace("<br>", ";").replace(",",";")
        else:
            Descriptions = re.search('<div class="preview-text  text-gray prose">        <div>(.*?)</div>', html)
            if Descriptions:
                descriptions = Descriptions.group(1).strip().replace("<br>", ";").replace(",",";")
            else:

                descriptions = "no descriptions"

        # 写入所有的文件
        with open("con_es2.txt","a")as f:
            f.write('good_id:%s, ' %goodId)
            f.write('good_url:%s, ' % url)
            f.write("pic:%s, "% img_url)
            f.write("title:%s, "%  title)
            f.write("price_now:%s, "% price_now)
            f.write("reviews:%s, "% feedback)
            f.write("favorites:%s, "%  favorited)

            f.write('shop_name:%s, ' % shop_name)
            f.write('shop_url:%s, ' % shop_url)
            f.write("descriptions:%s "% descriptions)
            f.write("\n")

        '''
        search得到的是对象如<_sre.SRE_Match object at 0x0300E770>
        加.group(0)显示匹配的所有字段
        .group(1)显示组一，以后一次类推
        '''
       
    else:
        print("没有访问到详情页")

    return goodId

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
    url='https://www.etsy.com/shop/VeryCharms/reviews?'
    headers = {
        'Host': 'www.etsy.com',
        'Referer': 'https://www.etsy.com/shop/VeryCharms/reviews',
        'upgrade-insecure-requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    res_cookies= get_cookie()
    res_cookies1 = get_cookie1()
    getFeedback(url,res_cookies)
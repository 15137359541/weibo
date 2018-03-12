import requests,re
def goods_list(url,cookies):
    response = requests.get(url=url,cookies=cookies,timeout=30)
    if response:
        # 商品id编号
        goodId = re.search('(\d+)', url).group(1).strip()
        # 简单处理详情页面
        html = response.content.decode("utf-8").replace('\n', '').replace('\r', '').replace('\t', '')
        # print(html)
        # 图片
        img_url = re.search('data-full-image-href="(.*?)"', html)
        # print('图片地址:',img_url.group(1))
        if img_url:
            img_url = img_url.group(1)
        else:
            img_url = "no img_url"
        # 标题
        title = re.search('<span itemprop="name">(.*?)</span>', html)
        if title:
            title = title.group(1)
        else:
            title = 'no title'
        # 价格,第一种情况，拥有现价，原价
        try:
            price = re.search(
                '<span id="listing-price" class="vertical-align-middle ">        <span>(.*?)</span>        <strike class="text-gray-lighter text-smallest normal">(.*?)</strike>',
                html)
            price_now = price.group(1).strip()
        # 价格，第二种情况，没有原价，只有现价
        except:
            try:
                print("进入第二种情况")
                price = re.search(
                    '<span id="listing-price" class="vertical-align-middle ">(.*?)<meta itemprop="currency" content="USD"/>',html)
                price_now = price.group(1).strip()
                print("价格是：",price_now)

            except:
                price_now = 0

        # 评论和喜欢的人
        feedback_loved = re.search(
            '<a href="#reviews">(.*?) reviews</a>(.*?)Favorited by: <a href="(.*?)">(.*?) people</a>', html)
        if feedback_loved:
            feedback = float((feedback_loved.group(1)))
            favorited = float(feedback_loved.group(4))
        else:
            feedback, favorited = "no feedback", 'no favorited'

        # 店铺名和店铺url；
        shopNameUrl = re.search('<a itemprop="url" href="(.*?)"><span itemprop="title">(.*?)</span></a>', html)
        # 店铺名有两种匹配规则
        if shopNameUrl:
            # 商电名
            shop_name = shopNameUrl.group(2)
            # 商电url:
            shop_url = shopNameUrl.group(1)
        else:
            shopNameUrl = re.search(
                '<a class="text-gray-darker" itemprop="url" href="(.*?)"><span itemprop="title">(.*?)</span></a>', html)
            if shopNameUrl:
                # 商电名
                shop_name = shopNameUrl.group(2)
                # 商电url:
                shop_url = shopNameUrl.group(1)
            else:
                shop_name, shop_url = 'no shop', ''
        # 描述
        Descriptions = re.search('<div class=" text-gray prose">        <div>(.*?)</div>', html)
        if Descriptions:
            descriptions = Descriptions.group(1).replace("<br>", ";").replace(",",";")
            # print(Descriptions.group(1).replace("<br>", ";"))
        else:
            Descriptions = re.search('<div class="preview-text  text-gray prose">        <div>(.*?)</div>', html)
            if Descriptions:
                descriptions = Descriptions.group(1).replace("<br>", ";").replace(",",";")
                # print(Descriptions.group(1).replace("<br>", ";"))
            else:

                descriptions = "no descriptions"

        # 写入所有的文件
        with open("con_es3.txt", "a")as f:
            f.write('good_id:%s, ' % goodId)
            f.write('good_url:%s, ' % url)
            f.write("pic:%s, " % img_url)
            f.write("title:%s, " % title)
            f.write("price_now:%s, " % price_now)
            f.write("reviews:%s, " % feedback)
            f.write("favorites:%s, " % favorited)

            f.write('shop_name:%s, ' % shop_name)
            f.write('shop_url:%s, ' % shop_url)
            f.write("descriptions:%s " % descriptions)
            f.write("\n")

        '''
        search得到的是对象如<_sre.SRE_Match object at 0x0300E770>
        加.group(0)显示匹配的所有字段
        .group(1)显示组一，以后一次类推
        '''

    else:
        print("没有访问到详情页")

url='https://www.etsy.com/listing/246733107/star-wars-millennium-falcon-laser?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sc_gallery-1-1&plkey=0dc4cad5dd55f61b96f8e4b6bbe44bf97981c840:246733107'

def get_cookie1():
    with open('cookie1.txt','r') as f:
        my_cookies1={}
        for line in f.read().split(';'):
            print (line)
            name,value=line.strip().split('=',1)  #1代表只分割一次
            my_cookies1[name]=value
        return my_cookies1

res_cookies1 = get_cookie1()
goods_list(url,res_cookies1)


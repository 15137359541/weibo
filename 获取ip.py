#coding=utf8
import requests
from bs4 import BeautifulSoup
import re
import os.path

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
headers = {'User-Agent': user_agent}


def getListProxies():
    session = requests.session()
    page = session.get("http://www.xicidaili.com/nn", headers=headers)
    soup = BeautifulSoup(page.text, 'lxml')

    proxyList = []
    taglist = soup.find_all('tr', attrs={'class': re.compile("(odd)|()")})
    for trtag in taglist:
        tdlist = trtag.find_all('td')
        proxy = {'http': tdlist[1].string + ':' + tdlist[2].string,
                 'https': tdlist[1].string + ':' + tdlist[2].string}
        url = "http://ip.chinaz.com/getip.aspx"  # 用来测试IP是否可用的url
        try:
            response = session.get(url, proxies=proxy, timeout=5)
            proxyList.append(proxy)
            if (len(proxyList) == 3):
                break
        except Exception, e:
            continue

    return proxyList
res=getListProxies()
print res
'''
[{'http': u'110.73.32.21:8123', 'https': u'110.73.32.21:8123'}, {'http': u'101.17.26.249:8118',
 'https': u'101.17.26.249:8118'}, {'http': u'121.31.176.166:8123', 'https': u'121.31.176.166:8123'},
  {'http': u'110.72.37.19:8123', 'https': u'110.72.37.19:8123'}, {'http': u'61.135.217.7:80', 
  'https': u'61.135.217.7:80'}, {'http': u'122.114.31.177:808', 'https': u'122.114.31.177:808'},
   {'http': u'122.225.17.123:8080', 'https': u'122.225.17.123:8080'}, {'http': u'182.38.253.140:8118',
    'https': u'182.38.253.140:8118'}, {'http': u'139.199.87.42:80', 'https': u'139.199.87.42:80'}, 
    {'http': u'121.31.196.221:8123', 'https': u'121.31.196.221:8123'}]
'''

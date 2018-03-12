#coding=utf8
from bs4 import BeautifulSoup
import requests
import random

def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list

def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies

if __name__ == '__main__':
    # url = 'http://www.xicidaili.com/nn/'
    # headers = {ddff
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    # }
    # ip_list = get_ip_list(url, headers=headers)
    # print("下面是ip_lsit")
    # print ip_list
    # proxies = get_random_ip(ip_list)
    # print(proxies)
    session = requests.session()
    # web_data = session.get("https://www.csdn.net/", proxies={'http': 'http://116.46.57.300:1123'},timeout=5)
    # print web_data
    # print web_data.text
    url = "http://ip.chinaz.com/getip.aspx"  # 用来测试IP是否可用的url

    response = session.get(url, proxies={'http': u'110.73.32.21:8123', 'https': u'110.73.32.21:8123'}, timeout=5)
    print response
    print response.text
# coding:utf-8
import requests
from bs4 import BeautifulSoup as bs
## 西刺代理 ---http://www.xicidaili.com/
def get_ip_list1():
    url = 'http://www.xicidaili.com/'
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'}
    res = requests.get(url, headers=headers)
    proxy_list = []
    soup = bs(res.text,'lxml')
    for i in range(1, 20):
        ip = soup.find_all('tr',{'class':'odd'})[i].find_all("td")[1].text
        port = soup.find_all('tr',{'class':'odd'})[i].find_all("td")[2].text
        address = str(ip)+':'+str(port)
        proxy_list.append(address)
        
    return proxy_list

## 讯代理 ---http://www.xdaili.cn/freeproxy.html
import requests
from bs4 import BeautifulSoup as bs

## DATA5U ---http://www.data5u.com/

## 66代理 ---http://www.66ip.cn/areaindex_6/1.html
def get_ip_list2():
    proxy_list =[]
    for index in range(1,9):
        url = 'http://www.66ip.cn/areaindex_{}/1.html'.format(index)
        res = requests.get(url)
        soup = bs(res.text,'lxml')
        
        # 爬取第一个IP代理
        for i in range(1,15):
            ip = soup.find_all('div',{'class':'footer'})[0].find_all('tr')[i].td.text
            port = soup.find_all('div',{'class':'footer'})[0].find_all('tr')[i].td.next_sibling.text
            address = str(ip)+':'+str(port)
            proxy_list.append(address)

    return proxy_list


## 快代理 ---http://www.kuaidaili.com/free/
def get_ip_list3():
    url = 'http://www.kuaidaili.com/free/inha/1/'
    res = requests.get(url)
    soup = bs(res.text,'lxml')
    proxy_list =[]
    # 爬取第一个IP代理
    for i in range(15):
        ip = soup.findAll('td',{'data-title':'IP'})[i].text
        port = soup.findAll('td',{'data-title':'PORT'})[0].text
        address = str(ip)+':'+str(port)
        proxy_list.append(address)
    return proxy_list
    
def get_all_proxy():
    content1 = get_ip_list1()
    content2 = get_ip_list2()
    content3 = get_ip_list3()
    proxy_list = content1 + content2 + content3
    
    return proxy_list
# coding:utf-8
from proxygetter import get_all_proxy
from proxytestter import myThread
from Mongodb import MongodbClient as MC




def main():
    proxy_list = get_all_proxy()
    i = 1
    for proxy in proxy_list:
        thread = myThread(proxy ,str(i))
        thread.start()
        i+=1
    print 'get proxy is done'

def refresh():
    db = MC('ip', 'localhost', 27017)
    proxys = db.getAll()
    i = 1
    for proxy in proxys:
        thread = myThread(proxy ,str(i))
        thread.start()
        i+=1
    print 'database proxy test is done'
    main() # 重新获取
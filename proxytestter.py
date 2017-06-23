# coding:utf-8
import requests
import threading
from  requests.exceptions import  ReadTimeout ,ConnectTimeout,ProxyError,ConnectionError,ChunkedEncodingError
from Mongodb import MongodbClient as MC






# 多线程测试
class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, proxy, name):
        threading.Thread.__init__(self)
        self.proxy = proxy
        self.name = name
        self.db = MC('ip', 'localhost', 27017)
        
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        print "Starting " +self.name
        if self.test_proxy():
            self.db.put(self.proxy) # 测试通过，就保存
        else:
            if self.db.find(self.proxy):
                self.db.delete(self.proxy)
                print '{} is deleting'.format(self.proxy)
            else:
                pass      #不通过，如果有这个数据就删除，否则就跳过
        print "Exiting " + self.name
        
    def test_proxy(self):

        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',\
        'authorization':'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'}

        try:

            proxies = {'http':self.proxy}
            test = requests.get('http://www.zhihu.com',proxies=proxies,headers=headers,timeout=5)

            if test.status_code == 200:
                
                print '{} is over test'.format(self.proxy)
                
                return True

            else:

                print '{} is remove'.format(self.proxy)

        except (ReadTimeout ,ConnectTimeout,ProxyError,ConnectionError,ChunkedEncodingError) as e:
            print e 
            print '{} is remove'.format(self.proxy)
        
        return False
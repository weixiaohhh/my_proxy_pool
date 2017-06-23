
爬虫代理池
=======




 

### 1、原理

通过爬取西刺，66，快代理等免费代理，多线程验证代理是否可用，然后存入Mongodb,利用apscheduler计时模块，来定时刷新数据库和检测数据库代理是否可用，用flask在本地服务器运行。


### 2、代理池设计

　　代理池由四部分组成:

* ProxyGetter:

　　代理获取接口，目前有5个免费代理源，每调用一次就会抓取这个5个网站的最新代理放入DB，可自行添加额外的代理获取接口；

* Mongodb:

　　用于存放代理IP

* Schedule:

　　计划任务用户定时去检测DB中的代理可用性，删除不可用的代理。同时也会主动通过ProxyGetter去获取最新代理放入DB；

* ProxyApi:



### 3、代码模块



* Api:

　　api接口相关代码，目前api是由Flask实现，代码也非常简单。客户端请求传给Flask，Flask调用ProxyManager中的实现，包括`get/delete/refresh/get_all`；

* DB:

　　数据库相关代码，目前数据库是采用SSDB。代码用工厂模式实现，方便日后扩展其他类型数据库；

* Manager:

　　`get/delete/refresh/get_all`等接口的具体实现类，目前代理池只负责管理proxy，日后可能会有更多功能，比如代理和爬虫的绑定，代理和账号的绑定等等；

* ProxyGetter:

　　代理获取的相关代码，目前抓取了[快代理](http://www.kuaidaili.com)、[代理66](http://www.66ip.cn/)、[有代理](http://www.youdaili.net/Daili/http/)、[西刺代理](http://api.xicidaili.com/free2016.txt)、[guobanjia](http://www.goubanjia.com/free/gngn/index.shtml)这个五个网站的免费代理，经测试这个5个网站每天更新的可用代理只有六七十个，当然也支持自己扩展代理接口；

* Schedule:

　　定时任务相关代码，现在只是实现定时去刷新代码，并验证可用代理，采用多进程方式；



### 4、安装

下载代码:
```
git clone https://github.com/weixiaohhh/my_proxy_pool.git

```

安装依赖:
```
pip install -r requirements.txt
```

启动:

```
运行main.py
>>>python main.py # 大概等待一俩分钟

>>>python ProxyApi.py # 打开接口

>>>>python scheduler.py # 新建cmd,用来定时更新

```

### 5、使用

    
    

　　爬虫中使用，如果要在爬虫代码中使用的话， 可以将此api封装成函数直接使用，例如:
```
import requests

def get_proxy():
    return requests.get("http://127.0.0.1:5000/get/").content

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5000/delete/?proxy={}".format(proxy))

# your spider code

def spider():
    # ....
    requests.get('https://www.example.com', proxies={"http": "http://{}".format(get_proxy())})
    # ....

```

　　测试地址：http://123.207.35.36:5000 单机勿压测。谢谢

### 6、最后
　　时间仓促，功能和代码都比较简陋，以后有时间再改进。喜欢的在github上给个star。感谢！

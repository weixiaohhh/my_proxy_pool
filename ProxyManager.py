
from Mongodb import MongodbClient as MC


class ProxyManager(object):
    def __init__(self):
        self.db = MC('ip', 'localhost', 27017)
        
    def get(self):
        return self.db.get()
        
    def getAll(self):
        return self.db.getAll()
        
    def delete(self, proxy):
        self.db.delete(proxy)
    
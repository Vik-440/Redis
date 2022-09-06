import redis
 
 
class redisOperation():
    def __init__(self, host='localhost', port=6379, db=0,password=""):
        self.database = redis.Redis(host=host, port=port, db=db, password=password)
        print("Successfully connect to Redis Server.")
 
    def setData(self, key, value):
        self.database.set(key, value)
 
    def getData(self, key):
        data = self.database.get(key)
        if data is None:
            return None
        else:
            return data.decode()
 
    def getKeys(self):
        byteKeys = self.database.keys()
        rawKeys = []
        for key in byteKeys:
            rawKeys.append(key.decode())
        return rawKeys


r = redisOperation()
r.setData('username', 'Vik-440')
print(r.getData('username'))
def foo():
    print(1)
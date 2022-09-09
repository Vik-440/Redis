from telnetlib import NOP
import redis
database = redis.Redis()
from dotenv import load_dotenv
import os

load_dotenv()
host = os.getenv("r_host")
port = os.getenv("r_port")
password = os.getenv("r_pass")
# redis_host = "AWS"
redis_host = "LOCAL"

class RedisCon:
    if redis_host == "LOCAL":
        def __init__(self, host='localhost', port=6379, db=0,password=""):
            self.database = redis.Redis(host=host, port=port, db=db, password=password)
            print("Successfully connect to LOCAL Redis Server.")
    elif redis_host == "AWS":
        def __init__(self, host=host, port=port, password=password):
            self.database = redis.Redis(host=host, port=port, password=password)
            print("Successfully connect to Redis Server AWS.")
 
    def setdata(self, key, value):
        data = self.database.set(key, value)
        return data
 
    def getdata(self, key):
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
    
    def getsetdata(self, key, value):
        data = self.database.getset(key, value)
        if data is None:
            return None
        else:
            return data.decode()
    
    def getrange(self, key, start, end):
        data = self.database.getrange(key, start, end)
        if data is None:
            return None
        else:
            return data.decode()

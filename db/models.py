import redis
database = redis.Redis()
from dotenv import load_dotenv
import os

load_dotenv()
host = os.getenv("r_host")
port = os.getenv("r_port")
password = os.getenv("r_pass")
# hr = redis.StrictRedis(
#     host=r_host,
#     port=r_port,
#     password=r_pass,
#     charset="utf-8",
#     decode_responses=True)


class RedisCon:
    def __init__(self, host=host, port=port, password=password):
        self.database = redis.Redis(host=host, port=port, password=password)
        print("Successfully connect to Redis Server.")
 
    def setdata(self, key, value):
        self.database.set(key, value)
 
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

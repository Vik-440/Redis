from dotenv import load_dotenv
import os
import redis
# from Back_end.redis_ex import foo
from db.redis_init import RedisCon


r = RedisCon()
print(r.setdata('index1', '111'))
r.setdata('index2', '12')
print(f"index: {r.getdata('index')}")
print(f"index1: {r.getdata('index1')}")
print(f"keys: {(r.getKeys())}")
print(f"index2: {r.getdata('index2')}")
print(f"test GETSET: {r.getsetdata('index2', '01234567890')}")
print(f"index2: {r.getdata('index2')}")
print(f"index2 (getrange): {r.getrange('index2', 1, 7)}")
print(f"index2: {r.getdata('index2')}")

# foo()
# load_dotenv()
# r_host = os.getenv("r_host")
# r_port = os.getenv("r_port")
# r_pass = os.getenv("r_pass")
# r = redis.StrictRedis(
#     host=r_host,
#     port=r_port,
#     password=r_pass,
#     charset="utf-8",
#     decode_responses=True)
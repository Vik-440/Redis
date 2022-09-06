from dotenv import load_dotenv
import os
import redis
# from Back_end.redis_ex import foo
from db.models import RedisCon


hr = RedisCon()
hr.setdata('index1', '11')
print(f"index: {hr.getdata('index')}")
print(f"index1: {hr.getdata('index1')}")

# foo()
# load_dotenv()
# r_host = os.getenv("r_host")
# r_port = os.getenv("r_port")
# r_pass = os.getenv("r_pass")
# hr = redis.StrictRedis(
#     host=r_host,
#     port=r_port,
#     password=r_pass,
#     charset="utf-8",
#     decode_responses=True)
from dotenv import load_dotenv
import os
import redis

load_dotenv()
r_host = os.getenv("r_host")
r_port = os.getenv("r_port")
r_pass = os.getenv("r_pass")
hr = redis.StrictRedis(
    host=r_host,
    port=r_port,
    password=r_pass,
    charset="utf-8",
    decode_responses=True
    )

hr.set('index', '1')
print(f"index: {hr.get('index')}")

# host_redis.set('ip_address', '127.0.0.0', 10)
# host_redis.set('timestamp', int(time.time()))
# host_redis.set('user_agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11)')
# host_redis.set('last_page_visited', 'home', 100)

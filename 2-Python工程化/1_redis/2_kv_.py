# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/26
# redis 资料： https://www.redis.net.cn/tutorial/3501.html
# redis 简单k v 操作。
import redis
import random
import time


conn = redis.Redis(host='81.70.197.234', port=26379, password='helloworld')
try:
	conn.ping()
except Exception as e:
	print("连接失败", str(e))
else:
	print("连接成功")


# conn.set("abc", random.random())  # 设置abc 的 值
# print(conn.get("abc"))

conn.set("abc", random.random(),3)
for i in range(10):
	print(conn.get("abc"))
	time.sleep(0.5)







# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/26
# redis 资料： https://www.redis.net.cn/tutorial/3501.html
# redis 简单k v 操作。
# redis 在web开发中，常用于作为缓存。
import redis
import random
import time


conn = redis.Redis(host='81.70.197.234', port=26379, password='helloworld', db=0)
try:
	conn.ping()  # 尝试连接
except Exception as e:
	print("连接失败", str(e))
else:
	print("连接成功")
print(conn.info())  # 获取redis信息 并打印









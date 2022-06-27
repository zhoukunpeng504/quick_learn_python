# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/27
# 写一个程序， 连接redis 从 list_nscc 中pop一个元素
# redis 参数：81.70.197.234:26379    密码 helloworld  db 1
import random
import redis
import time


conn = redis.Redis(host='81.70.197.234', port=26379, password='helloworld', db=1)
try:
	conn.ping()  # 尝试连接
except Exception as e:
	print("连接失败", str(e))
else:
	print("连接成功")




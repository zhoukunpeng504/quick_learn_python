# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/26
# 学习利用redis实现多进程通信。
# redis 资料： https://www.redis.net.cn/tutorial/3501.html
# redis 简单k v 操作。
import redis


conn = redis.Redis(host='81.70.197.234', port=26379, password='helloworld')
try:
	conn.ping()
except Exception as e:
	print("连接失败", str(e))
else:
	print("连接成功")






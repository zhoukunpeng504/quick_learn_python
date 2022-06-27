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

conn.delete('list_study')   # 清除
conn.lpush("list_study", 1)  # 把1 放入list_study中
res = conn.lrange('list_study', 0 , -1) # 获取放入list_study中的所有内容
print(res)
conn.lpush('list_study', 2)    # 把 2 放入
print(conn.lrange('list_study', 0 , -1))  # 获取所有
print(conn.lpop('list_study'))   # 弹出1个元素
print(conn.lpop('list_study'))   # 弹出2个元素
print(conn.lpop('list_study'))   # 弹出3个元素








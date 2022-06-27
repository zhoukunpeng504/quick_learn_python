# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/26
# redis zset.（zset 可以理解为 排行榜）
# redis 资料： https://www.redis.net.cn/tutorial/3501.html
# redis zset简单操作。
# 读取student_score.txt中的信息， 用zset输出倒数10名  和 正数10名
import redis


conn = redis.Redis(host='81.70.197.234', port=26379, password='helloworld')
try:
	conn.ping()
except Exception as e:
	print("连接失败", str(e))
else:
	print("连接成功")

with open("student_score.txt", "r") as f:
	student_info = f.read().splitlines()


for line in student_info:
	name,cn_score,math_score = line.split(",")
	score = int(cn_score) + int(math_score)
	conn.zadd("score_rank", {name:score})

res = conn.zrange('score_rank',0, 10, withscores=True)
print("倒数1-10名如下：")
for name, score in res:
	print(f"姓名：{name.decode('utf-8')} 总分：{score}")  # 利用f字符串输出

res = conn.zrevrange('score_rank',0, 10, withscores=True)
print("正数1-10名如下：")
for name, score in res:
	print(f"姓名：{name.decode('utf-8')} 总分：{score}")  # 利用f字符串输出






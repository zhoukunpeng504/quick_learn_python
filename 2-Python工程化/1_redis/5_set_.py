# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/26
# redis set
# redis 资料： https://www.redis.net.cn/tutorial/3501.html
# redis 集合简单操作。sadd  smembers  sismember
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
	name = line.split(",")[0]
	conn.sadd("names", name)

s_members = conn.smembers('names') #
for name in s_members:
	# 其返回的序列中 每个元素都是bytes对象， bytes打印之前，先调用decode方法 转化为str
	print(name.decode('utf-8'))

# 判断王五是否在集合中
print(conn.sismember('names', '王五'))








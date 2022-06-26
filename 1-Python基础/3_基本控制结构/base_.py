# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/24
# 基本控制结构
# if else 结构
# for  while  循环结构
# try  except 异常捕获结构

# for 循环 或者 while 循环中，如果含有else语句，循环没有被强制终止，else才能执行。
for i in range(1,10):
	if i == 9:
		break
else:
	print("aaa")


# 异常捕获
import traceback
try:
	assert 1==2,Exception("error!")
except Exception as e:
	print("catch exception", str(e))
	# 打印引起异常的具体信息
	traceback.print_exc()


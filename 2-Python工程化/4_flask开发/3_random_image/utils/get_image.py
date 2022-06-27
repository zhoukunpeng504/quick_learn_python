# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/27
import os
import random

my_path = os.path.abspath(os.path.dirname(__file__))
image_buff = []
for file_name in os.listdir(my_path):
	if file_name.endswith(".jpg"):
		with open(os.path.join(my_path, file_name), "rb") as f:
			image_buff.append(f.read())

def random_get_image():
	# 随机获取图片
	return random.choice(image_buff)


if __name__ == '__main__':
	print("try....")
	image_content = random_get_image()
	print(type(image_content), len(image_content))
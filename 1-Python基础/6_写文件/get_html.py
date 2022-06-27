# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/27
# 利用requests 发起http请求， 并把返回的字符串写入到文件
import requests


baidu_img_url = 'https://www.baidu.com/'
resp = requests.get(baidu_img_url, timeout=3)
with open("baidu.html", "wb") as f:
	f.write(resp.content)

# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/27
# 利用requests 发起http请求， 并把返回的字节流写入到文件
import requests


baidu_img_url = 'https://fyb-pc-static.cdn.bcebos.com/static/asset/homepage@2x_7926b0bf1e591ee96d2fc68b3a8a1ee0.png'
resp = requests.get(baidu_img_url, timeout=3)
with open("baidu_image.png", "wb") as f:
	f.write(resp.content)
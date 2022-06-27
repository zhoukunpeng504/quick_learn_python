# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/27
import requests

resp = requests.get("http://127.0.0.1:5000/image")
with open("image.jpg", "wb") as f:
	f.write(resp.content)

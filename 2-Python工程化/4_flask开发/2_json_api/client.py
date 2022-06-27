# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/27
import requests


rsp = requests.get("http://127.0.0.1:5000/json")
res = rsp.json()
print(res, type(res))

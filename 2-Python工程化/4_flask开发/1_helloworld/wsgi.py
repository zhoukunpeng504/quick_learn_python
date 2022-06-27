# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/27
# flask 版 hello world
from flask import Flask, request, Response
import json
import datetime


app = Flask(__name__)  # 创建一个app对象。  后续所有的核心操作都在app对象上执行

# 通过app.route装饰器绑定一个路由规则。对url路径等于/ 的， 执行index函数，并把结果返回给客户端。
@app.route("/", methods=['GET', 'POST'])
def index():
	# 返回 hello world
	return 'hello world'

app.run()

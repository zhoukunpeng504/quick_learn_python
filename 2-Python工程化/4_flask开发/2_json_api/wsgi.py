# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/27
# 前后端之间  后端服务之间通信用的最多的方式 就是 json接口。
from flask import Flask, request, Response
import json
import datetime


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
	return 'hello world'



@app.route("/json", methods=['GET', 'POST'])
def index():
	# 返回一个JSON数据
	now = datetime.datetime.now()
	result = {'status': True,'data': str(now)}
	return Response(json.dumps(result), content_type="application/json")


app.run()

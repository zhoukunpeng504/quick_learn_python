# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/27
from flask import Flask, request, Response
import json
import datetime
from utils import get_image


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
	return 'hello world'



@app.route("/json", methods=['GET', 'POST'])
def _json():
	# 返回一个JSON数据
	now = datetime.datetime.now()
	result = {'status': True,'data': str(now)}
	return Response(json.dumps(result), content_type="application/json")


@app.route("/image", methods=['GET', 'POST'])
def image():
	# 随机返回一个jpg图片
	return Response(get_image.random_get_image(), content_type="image/jpg")


app.run()



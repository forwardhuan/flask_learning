#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/')  # 路由
def hello_word():  # 视图函数 mtv： view 视图 函数
    return 'Hello Word'


def index():
    return 'index'


app.add_url_rule('/index/', view_func=index)

data = {'a': '北京', 'b': "上海", 'c': "深圳"}


@app.route('/getcity/<key>')
def get_city(key):
    return data.get(key)


@app.route('/add/<int:num>')
def add(num):
    return str(num)


@app.route('/add1/<float:money>')
def add1(money):
    return str(money)


@app.route('/index/<path:p>')
def get_path(p):
    print('****', type(p))
    return p


@app.route('/test/<uuid:uid>') # 必须uuid格式， uuid模块
def test(uid):
    print("*****", type(uid))
    return '唯一标识'


if __name__ == '__main__':
    print()
    app.run()

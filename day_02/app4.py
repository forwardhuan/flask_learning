#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/index')
def index():
    print(request.headers)
    return "welcome everyone"


@app.route('/register')
def register():
    r = render_template('register.html')
    return r


@app.route('/register2', methods=['GET', "POST"])
def register2():  # 获取提交到的内容
    print(request.full_path)
    print(request.path)
    print(request.args)
    print(request.form)
    return "进入"


if __name__ == '__main__':
    print(app.url_map)  # 路由规则表
    app.run()

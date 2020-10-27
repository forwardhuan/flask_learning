#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/projects/')  # 路由中末尾如果添加了'/'，如果找不到会进行重定向
def projects():
    return 'The project page'


@app.route('/about')  # 请求路由中如果添加了 '/'，会显示 not found
def about():
    return 'The about page'


if __name__ == '__main__':
    print()
    app.run()

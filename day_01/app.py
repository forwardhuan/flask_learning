#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask
import settings

# WSGI: Python Web Server Gateway Interface
app = Flask(__name__)

# 导入默认配置
app.config.from_object(settings)


# 装饰器
@app.route('/')  # 路由
def hello_word():  # 视图函数 mtv： view 视图 函数
    return 'Hello Word'


if __name__ == '__main__':
    # debug:bool
    #     true:适用于开发模式，自动检测代码 Development
    #     false:适用于生产模式，开发完成 Prouction
    app.run(host='0.0.0.0', port=5000)
    # flask 内置服务器 nqinx

# 环境
# production, development, testing

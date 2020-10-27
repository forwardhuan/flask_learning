#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, Response, make_response
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/index')
def index():
    return {'a': '北京', 'b': "上海", 'c': "深圳"}  # Content-Type: application/json


@app.route('/index1')
def index1():
    return '北京'  # Content-Type: text/html


@app.route('/index2')
def index2():
    return Response(('北京', '上海'))  # Content-Type: text/html


@app.route('/index3')
def index3():
    content = """
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>首页</title>
        <style>
            div{
                width:100%,
                height:100px,
                border:2px solid red
            }
        </style>
    </head>
    <body>
    <h1>欢迎来到淘宝首页</h1>
    <div>
        <ul>
            <li>hello</li>
            <li>abc</li>
        </ul>
    </div>
    </body>
    </html>
    """
    response = make_response(content)
    return response


if __name__ == '__main__':
    app.run()

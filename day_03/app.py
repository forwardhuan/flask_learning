#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template, redirect, url_for
import settings
import json

app = Flask(__name__)
app.config.from_object(settings)

users = []


@app.route('/', endpoint='index')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = request.form
        username = form.get('username')
        password = form.get('password')

        user = {'username': username, 'password': password}
        users.append(user)
        # return '注册成功! <a href="/">返回首页</a>'
        return redirect(url_for('index'))
    return render_template('register.html')


@app.route('/show')
def show():
    return render_template('show.html', users=users)


@app.route('/test')
def test():
    url = url_for('index')  # 路径反向解析
    print(url)
    return "Test"


if __name__ == '__main__':
    app.run()

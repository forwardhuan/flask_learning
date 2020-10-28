#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template, redirect, url_for
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/show')
def show():
    girls = ['zhang', 'zhao', 'li']
    users = [
        {'username': "Jack", 'password': '123'},
        {'username': "Tom", 'password': '123'},
        {'username': "Jone", 'password': '123'},
        {'username': "mack", 'password': '123'}
    ]
    msg = '<h1>你好</h1>'
    n1 = 'hello'
    return render_template('show2.html', users=users, girls=girls, msg=msg, n1=n1)


if __name__ == '__main__':
    app.run()

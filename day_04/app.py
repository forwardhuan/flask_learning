#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template, redirect, url_for
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/')
def index():
    msg = 'hello word hello'
    return render_template('define_filter.html', msg=msg)


def replace_hello(value):
    print('---->', value)
    value = value.replace('hello', '')
    print('====>', value)
    return value.strip()


app.add_template_filter(replace_hello, name='replace')


@app.add_template_filter('list_reverse')
def reverse_list(li):
    temp_li = list(li)
    temp_li.reverse()
    return temp_li


if __name__ == '__main__':
    app.run()

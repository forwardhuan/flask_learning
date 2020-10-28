#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template, redirect, url_for
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/base')
def load_base():
    return render_template('base.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/macro')
def use_macro():
    return render_template('macro_use.html')


if __name__ == '__main__':
    app.run()

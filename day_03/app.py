#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/add/<int:n1>/<int:n2>')
def add(n1, n2):
    if n1 > 0 and n2 > 0:
        r = n1 + n2
        return str(r)
    else:
        return '-1'


if __name__ == '__main__':
    app.run()

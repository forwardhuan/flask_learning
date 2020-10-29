#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask

import settings
from apps.user.view import user_bp


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')  # app是一个核心对象
    app.config.from_object(settings)
    app.register_blueprint(user_bp)
    print(app.url_map)
    return app

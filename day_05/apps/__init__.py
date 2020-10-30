#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask

import settings
from apps.user.view import user_bp
from exts import db


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')  # app是一个核心对象
    app.config.from_object(settings.DevelopmentConfig)
    # 注册蓝图
    app.register_blueprint(user_bp)
    # 将db对象于app进行关联
    db.init_app(app)
    return app

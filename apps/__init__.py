#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask
import settings
from apps.article.view import article_bp
from apps.goods.view import goods_bp
from apps.user.view import user_bp
from exts import db, bootstrap


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings.DevelopmentConfig)
    db.init_app(app=app)
    # 初始化bootstrap
    bootstrap.init_app(app=app)
    app.register_blueprint(user_bp)
    app.register_blueprint(article_bp)
    # app.register_blueprint(goods_bp)
    return app

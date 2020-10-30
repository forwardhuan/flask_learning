#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask
import settings
from apps.user.view import user_bp
from exts import db


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings.DevelopmentConfig)
    db.init_app(app=app)
    app.register_blueprint(user_bp)
    return app

#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Config:
    # mysql.md+pymysql://user:password@hostip:port/databasename
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/flaskblog'
    # 是否有警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 是否是调试模式
    SQLALCHEMY_ECHO = True


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False

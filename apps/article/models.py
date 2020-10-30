#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from datetime import datetime

from exts import db


class ArticleType(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    type_name = db.Column(db.String(20), nullable=False)


class Article(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    p_datetime = db.Column(db.DATETIME, default=datetime.now)
    click_num = db.Column(db.INTEGER, default=0)
    save_num = db.Column(db.INTEGER, default=0)
    love_num = db.Column(db.INTEGER, default=0)

    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id'), nullable=False)
    type_id = db.Column(db.INTEGER, db.ForeignKey('article_type.id'), nullable=False)
    comments = db.relationship('Comment', backref='article')


class Comment(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    comment = db.Column(db.String(255), nullable=False)
    c_datetime = db.Column(db.DATETIME, default=datetime.now)

    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id'))
    article_id = db.Column(db.INTEGER, db.ForeignKey('article.id'))

    def __str__(self):
        return self.comment

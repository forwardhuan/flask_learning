#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from exts import db


class Goods(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.INTEGER)
    users = db.relationship('User', backref='goods_list', secondary='user_goods')

    def __str__(self):
        return self.g_name


# tags = db.Table('tags',
#                 db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
#                 db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
#                 )


class UserGoods(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id'))
    goods_id = db.Column(db.INTEGER, db.ForeignKey('goods.id'))
    number = db.Column(db.INTEGER, default=1)

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from datetime import datetime

from exts import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(11), nullable=True)
    isdelete = db.Column(db.BOOLEAN, default=False)
    rdatetime = db.Column(db.DateTime, default=datetime.now())

    def __str__(self):
        return self.username

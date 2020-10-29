#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class User(object):
    def __init__(self, username, password, phone=None):
        self.username = username
        self.password = password
        self.phone = phone

    def __str__(self):
        return self.username

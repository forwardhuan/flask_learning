#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Blueprint, request, redirect, render_template

from apps.user.model import User
from exts import db

user_bp = Blueprint('user', __name__)


@user_bp.route('/register', endpoint='register', methods=['POST', 'GET'])
def register():
    print(request.method)
    if request.method == "POST":
        form = request.form
        username = form.get("username")
        password = form.get("password")
        repassword = form.get("repassword")
        phone = form.get("phone")
        if password == repassword:
            user = User()
            user.username = username
            user.password = password
            user.phone = phone
            db.session.add(user)
            db.session.commit()
            return "用户注册成功"
        else:
            return "两次密码不一致"
    else:
        return render_template('user/register.html')

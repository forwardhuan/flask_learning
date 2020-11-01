#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Blueprint, redirect, request, render_template, url_for, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash

from apps.user.models import User
from exts import db

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/')
def index():
    # uid = request.cookies.get('uid', type=int)
    uid = session.get('uid')
    print(uid)
    if uid is not None:
        user = User.query.filter(User.id.__eq__(uid)).first()

        return render_template('user/index.html', user=user)
    return render_template('user/index.html')


@user_bp.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        rePassword = request.form.get('repassword')
        phone = request.form.get('phone')
        email = request.form.get('email')
        if password == rePassword:
            user = User()
            user.username = username
            user.password = generate_password_hash(password)
            print(len(user.password))
            user.phone = phone
            user.email = email
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.index'))
        else:
            return render_template('user/register.html', msg='两次密码不相同')
    else:
        return render_template('user/register.html')


# 手机号码验证
@user_bp.route('/checkphone', methods=["POST", "GET"])
def check_phone():
    phone = request.args.get('phone')
    print(phone)
    user = User.query.filter(User.phone.__eq__(phone)).all()

    print(user)
    # code: 400 不能用 200 能用
    if user is not None:
        return jsonify(code=400, msg='此号码已经注册')
    else:
        return jsonify(code=200, msg='此号码可以使用')


@user_bp.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(password)
        u_list = User.query.filter(User.username.__eq__(username)).all()
        print(u_list)
        for user in u_list:
            flag = check_password_hash(user.password, password)
            print(flag)
            if flag is True:
                # 1.cookie
                # res = redirect(url_for('user.index'))
                # res.set_cookie('uid', str(user.id), max_age=30 * 60)
                # return res
                # 2.session机制， session当成字典使用
                session['uid'] = user.id
                return redirect(url_for('user.index'))
            else:
                return render_template('user/login.html', msg='用户名或密码错误')
        else:
            return render_template('user/login.html', msg='用户名或密码错误')
    else:
        return render_template('user/login.html')


@user_bp.route('/logout')
def logout():
    res = redirect(url_for('user.index'))
    # res.delete_cookie('uid')
    session.pop('uid')
    return res

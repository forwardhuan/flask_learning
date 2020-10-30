#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Blueprint, request, render_template, redirect, url_for
from .model import User

user_bp = Blueprint('user', __name__)

# users = [User("Jack", "1234", "13937119999"),
#          User("Tome", "wwww", "13823111332")]


@user_bp.route('/', endpoint='home')
def user_center():
    return render_template('user/show.html', users=users)


@user_bp.route('/register', methods=['GET', 'POST'], endpoint='register')
def register():
    if request.method == 'POST':
        form = request.form
        username = form.get('username')
        password = form.get('password')
        repassword = form.get('repassword')
        phone = form.get('phone')
        if password == repassword:
            for user_tmp in users:
                if user_tmp.username == username:
                    return render_template('user/register.html', msg='用户已存在')
            # 创建User
            user = User(username, password, phone)
            users.append(user)
            return redirect(url_for('user.home'))
        else:
            return render_template('user/register.html', msg='两次密码不一致')
    else:
        return render_template('user/register.html')


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    return '用户登录'


@user_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    return '用户退出'


@user_bp.route('/del')
def del_user():
    username = request.args.get('username')
    for user in users:
        if user.username == username:
            users.remove(user)
            return redirect(url_for('user.home'))
    else:
        return '删除失败'


@user_bp.route('/update', methods=['GET', 'POST'], endpoint='update')
def update_user():
    if request.method == "POST":
        realname = request.form.get('realname')
        username = request.form.get('username')
        phone = request.form.get('phone')
        for user in users:
            if user.username == realname:
                user.username = username
                user.phone = phone
        return '更改成功'
    else:
        username = request.args.get('username')
        for user in users:
            print(user.password)
            if user.username == username:
                print(user)
                return render_template('user/update.html', user=user)
        else:
            return ""

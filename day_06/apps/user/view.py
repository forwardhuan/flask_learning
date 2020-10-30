#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import hashlib
from flask import Blueprint, request, render_template, redirect, url_for
from sqlalchemy import or_, and_

from apps.user.model import User
from exts import db

user_bp = Blueprint('user', __name__)


@user_bp.route('/', endpoint='home')
def user_center():
    # 查询数据库中的数据
    users = User.query.filter(User.isdelete.__eq__(False)).all()
    return render_template('user/center.html', users=users)


@user_bp.route('/register', endpoint='register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        form = request.form
        username = form.get("username")
        password = form.get("password")
        repassword = form.get("repassword")
        phone = form.get("phone")
        if password == repassword:
            # 注册用户
            user = User()
            user.username = username
            user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            user.phone = phone
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.home'))
        else:
            return "两次密码不一致"
    else:
        return render_template('user/register.html')


@user_bp.route('/login', endpoint='login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        form = request.form
        username = form.get('username')
        password = form.get('password')
        new_pwd = hashlib.sha256(password.encode('utf-8')).hexdigest()
        ulist = User.query.filter_by(username=username)
        print(ulist)
        for u in ulist:
            print(u.id)
            if u.password == new_pwd:
                return redirect(url_for('user.home'))
        else:
            return render_template('user/login.html', msg='用户名或密码错误')
    else:
        return render_template('user/login.html')


@user_bp.route('/search')
def search():
    keyword = request.args.get('search')
    ulist = User.query.filter(or_(User.username.contains(keyword), User.phone.contains(keyword))).all()
    return render_template('user/center.html', users=ulist)


@user_bp.route('/update', endpoint='update', methods=["POST", "GET"])
def update_user():
    if request.method == "POST":
        userid = request.form.get('id')
        username = request.form.get('username')
        phone = request.form.get('phone')
        user = User.query.get(userid)
        user.username = username
        user.phone = phone
        db.session.commit()
        return redirect(url_for('user.home'))
    else:
        user_id = request.args.get('id')
        user = User.query.get(user_id)
        return render_template('user/update.html', user=user)


@user_bp.route('/del', endpoint='delete')
def delete():
    user_id = request.args.get('id')
    user = User.query.get(user_id)
    # # 1. 逻辑删除
    # user.isdelete = True
    # # 提交
    # db.session.commit()
    # 2. 物理删除
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user.home'))


@user_bp.route('/test')
def test():
    username = request.args.get('username')
    user = User.query.filter_by(username=username).first()
    print(user.username, user.rdatetime)

    return 'test'


@user_bp.route('/select')
def user_select():
    user = User.query.get(1)  # 根据主键查询用户
    # user1 = User.query.filter(User.username == 'ggg').all()
    # user1 = User.query.filter(and_(User.username == 'ggg', User.phone.startswith('137'))).all()
    # user1 = User.query.order_by('username').all()
    # user1 = User.query.order_by(-User.username).all()
    # limit + offset
    # user1 = User.query.order_by('id').limit(2).all()
    user1 = User.query.order_by('id').offset(2).limit(2).all()
    return render_template('user/select.html', user=user, user1=user1)

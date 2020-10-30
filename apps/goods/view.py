#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for

from apps.goods.models import Goods, UserGoods
from apps.user.models import User
from exts import db

goods_bp = Blueprint('goods', __name__)


# 用户找商品
@goods_bp.route('/findgoods')
def find_goods():
    uid = request.args.get('uid')
    user = User.query.get(uid)
    return render_template('goods/findgoods.html', user=user)


@goods_bp.route('/finduser')
def find_user():
    gid = request.args.get('gid')
    goods = Goods.query.get(gid)
    return render_template('goods/finduser.html', goods=goods)


@goods_bp.route('/show')
def show():
    users = User.query.filter(User.is_delete.__eq__(False)).all()
    goods = Goods.query.all()
    return render_template('goods/show.html', users=users, goods=goods)


@goods_bp.route('/buy')
def buy():
    uid = request.args.get('uid')
    gid = request.args.get('gid')
    ug = UserGoods()
    ug.user_id = uid
    ug.goods_id = gid
    db.session.add(ug)
    db.session.commit()
    return "购买成功"

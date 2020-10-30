#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for

from apps.article.models import Article
from apps.user.models import User
from exts import db

article_bp = Blueprint('article', __name__)


@article_bp.route('/publish', endpoint='public', methods=["POST", "GET"])
def public_article():
    if request.method == "POST":
        form = request.form
        title = form.get('title')
        content = form.get('content')
        uid = form.get('uid')
        print(uid)
        article = Article()
        article.title = title
        article.content = content
        article.user_id = uid
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('article.all'))
    else:
        users = User.query.filter(User.is_delete.__eq__(False)).all()
        return render_template('article/add_article.html', users=users)


@article_bp.route('/all', endpoint='all')
def article_all():
    articles = Article.query.all()
    return render_template('article/all.html', articles=articles)


@article_bp.route('/all1')
def all_article1():
    user_id = request.args.get('id')
    user = User.query.get(user_id)
    return render_template('article/all1.html', user=user)

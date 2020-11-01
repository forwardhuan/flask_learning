#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Blueprint, redirect, request, render_template, url_for

user_bp1 = Blueprint('user', __name__, url_prefix='/user')


@user_bp1.route('/')
def index():
    return render_template('base.html')

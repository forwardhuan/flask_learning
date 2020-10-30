#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Blueprint, redirect, request, render_template, url_for

user_bp = Blueprint('user', __name__)

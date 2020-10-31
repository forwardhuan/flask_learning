#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from apps.user.models import User
from apps.article.models import *
from apps.goods.models import *
from apps import create_app
from exts import db

app = create_app()

manage = Manager(app=app)
migrate = Migrate(app=app, db=db)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()

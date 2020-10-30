#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from apps.user.model import User, UserInfo
from apps import create_app
from exts import db

app = create_app()

manager = Manager(app=app)

# 命令工具
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)


@manager.command
def init():
    """
    init
    """
    print('初始化')


if __name__ == '__main__':
    manager.run()

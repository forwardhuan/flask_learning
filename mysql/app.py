#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from apps.user.model import User
from apps import create_app
from exts import db

app = create_app()
manager = Manager(app=app)

migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)


@manager.command
def init():
    """
    init
    """
    pass


if __name__ == '__main__':
    manager.run()

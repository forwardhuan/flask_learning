### flask-script

> pip install flask-script

使用里面的Manager进行命令得到管理和使用
manager = Manger(app=app)

使用命令在终端
> python app.py runserver

> python app.py runserver -h 0.0.0.0 -p 5000

自定义添加命令：
```python
@manager.command
def init():
    print('初始化')
```

python app.py init

### 数据库
mtv
- model 模型 ---> 数据库
- template 模板
- view 视图

安装:
> pip install pymysql   建公路
> pip install flask-sqlalchemy  实现ORM映射
> pip install flask-migrate 发布命令工具


sqlalchemy: ORM,映射关系
flask-sqlalchemy:基于sqlalchemy，做了进一步的封装，是程序员在开发的时候更加方便



1.配置数据库的连接路径
```
# mysql+pymysql://user:password@hostip:port/databasename
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/flaskday05'
```

2.创建包ext
__init__.py添加

db = SQLAlchemy() ---> 必须跟app关联

```python
def create_app():
    ...
    db.init_app(app)
    return app
```

3.migrate
```python
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)
```

4. 创建模型
models.py
    
模型就是类
    
```
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(12), nullable=False)
    phone = db.Column(db.String(11), unique=True)
    rdatetime = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.username
```

5.使用命令：
a. 敲黑板 。。。
    在app.py 中导入模型: from apps.user.model import User
b. 在终端使用命令：db
    python app.py db init --> 产生一个文件夹 migrations
    python app.py db migrate --> 自动产生一个版本文件
    项目
      | ---apps
      | ---ext
      | ---migrations  python app.py db init
           | --- versions 版本文件夹
                |---4d1262887c30_.py  ---> python app.py db migrate
                |---53f9c41119d8_.py  
                                        python app.py db upgrade
                                        python app.py db downgrade                                      



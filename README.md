[flask-sqlalchemy说明文档](http://www.pythondoc.com/flask-sqlalchemy/index.html)

### 一对多
- User
```
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(30))
    icon = db.Column(db.String(100))
    is_delete = db.Column(db.BOOLEAN, default=False)
    r_datetime = db.Column(db.DateTime, default=datetime.now)

    # 增加一个字段
    articles = db.relationship('Article', backref='user', lazy='dynamic')
```

- Article
```
class Article(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    p_datetime = db.Column(db.DATETIME, default=datetime.now)
    click_num = db.Column(db.INTEGER, default=0)
    save_num = db.Column(db.INTEGER, default=0)
    love_num = db.Column(db.INTEGER, default=0)

    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id'), nullable=False)
```

### 多对多
```
class Goods(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.INTEGER, nullable=False)
    users = db.relationship('User', backref='goods_list', secondary='user_goods')

    def __str__(self):
        return self.g_name
```

```
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(30))
    icon = db.Column(db.String(100))
    is_delete = db.Column(db.BOOLEAN, default=False)
    r_datetime = db.Column(db.DateTime, default=datetime.now)

    # 增加一个字段
    articles = db.relationship('Article', backref='user', lazy='dynamic')
```

```
# 关联User表和Goods表
class UserGoods(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id'))
    goods_id = db.Column(db.INTEGER, db.ForeignKey('goods.id'))
    number = db.Column(db.INTEGER, default=1)
```
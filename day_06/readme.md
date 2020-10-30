1. 查询
查询所有： 模型类.query.all() ~ select * from user;
有条件的查询：
    模型类.query.filter_by(字段名=值) ~ select * from user where 字段=值;
    模型类.query.filter_by(字段名=值).first() ~ select * from user where 字段=值 limit(1);

select * from user where age>17 and gender='男';
select * from user where username like 'zhang%';
select * from user where rdatetime > XXX and rdatetime < XXX;

    模型类.query.filter() 里面是布尔的条件
    模型类.query.filter_by() 里面是一个等值
    
**** 模型类 ****
User.query.filter(User.username.startswith('g')).all() -> select * from user where username like 'g%';

User.query.get(pk)
User.query.all()
User.query.filter()
User.query.filter_by()

多条件
- User.query.filter(or_(User.username == 'ggg', User.phone.startswith('137')))
- User.query.filter(and_(User.username == 'ggg', User.phone.startswith('137')))

排序:order_by
- user1 = User.query.order_by('username').all()  字符串，不能倒序
- user1 = User.query.order_by(-User.username).all() 字段名，可以倒序

限制：limit
user1 = User.query.order_by('id').limit(2).all() 获取前两条记录
user1 = User.query.order_by('id').offset(2).limit(2).all() 跳去两条再获取两条记录
### 自定义过滤器
1. 通过flask模块中的add_template_filter方法
2. 使用装饰器完成

### 模板复用
#### 模板继承
- 多个模板具有完全相同的顶部和底部
- 多个模板具有相同的模板内容，但是内容中部分不一样
- 多个模板具有完全相同的模板内容

#### 标签
{% block 名字 %}
{% endblock %}
- 定义父模板
- 子模版继承父模板
步骤：
父模板：
1. 定义一个base.html的模板
2.分析模板中哪些是变化的，比如：{% block title %} 父模板的title {% endblock %}
   对变化的部分用block进行'预留位置'， 也称作挖坑
3. 注意： 样式和模板 需要提前预留

子使用父模板:
1. {% extends '父模板的名称' %}将父模板继承过来
2. 找到对应的block（坑）填充，每一个block都是有名字的


- include 包含
在A,B,C页面都共有的部分，但是其它页面没有这部分
这个时候考虑使用include
步骤：
1.先定义一个公共的模板部分，xxx.html
2.谁使用则include过来， {% include '文件夹/xxx.html' %}

- 宏 macro
1. 把它看作是jinja2的一个函数，这个函数可以返回一个html字符串
2. 目的：代码可以服用，避免代码冗余

定义有两种方式
1.在模板当中直接定义：
2.将所有的宏提取到一个模板中
```
{% import 'macro/macro.html' as aaa %}
{{ aaa.form('/') }}
```

变量声明
- 全局
```
{% set username='zhangsan' %}

{{ username }}
```

- 局部
```
{% with num=10 %}
    {{ num }}
{% endwith %}
```


总结：
变量： {{ 变量 }}
块：
{% if 条件 %} ... {% endif %}
{% for i in j %} ... {% endfor %}
{% block title %} ... {% endblock %}
{% macro func %} ... {% endmacro %}

{% include '' %}
{% import '' %}
{% extends '' %}

{{ url_for('static', filename=') }}

view:
@app.route('/'. endpoint='', methods=['GET','POST'])

template:

model:
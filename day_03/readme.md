### 路由
```python
@app.route('/')
def hello_word():
    return 'hello word'
```
### 视图函数的返回值
response响应
- str 自动转成response对象
- dict json
- response对象 response对象
- make_response response对象
- redirect() 重定向 302状态码
- render_template() 模板渲染 + 模板 

### 模板
1. if
```
{% if 条件 %}

{% endif %}
```

2. for
```
{% for 变量 in 可迭代对象 %}
    for循环要做的任务
{% endfor %}
```

可以使用loop变量
loop.index 序号从1开始
loop.index0 序号从0开始
loop.revindex 序号是倒着的
loop.revindex0 序号是倒着的，到0

### 过滤器
过滤器的本质就是函数
模板语法中过滤器:
```
{{ 变量名|过滤器(*args) }}

{{ 变量名|过滤器() }}
```

常见过滤器
- safe 禁止转义， 渲染内容中的标签不想让其转义
```
<p>{{ msg|safe }}</p>
```
- capitalize 首字母大写
- lower 全部小写
- upper 全部大写
- title 一句话中的首字母大写
- reverse 翻转
- format 格式化
```
{{ '%s is %d' |format('Lily','18') }}
``` 
- truncate 字符串截断

列表
- first
- last
- length
- sum
- sort

dict
- values()
- keys()
- items()
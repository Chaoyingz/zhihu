Django 仿知乎

## 简介
项目采用前后端分离开发模式。

后端主要采用Django-rest-framework开发来提供API，配合corsheaders、django_filters分别实现跨域、过滤功能。前端采用基于Vue的服务端渲染框架Nuxt进行开发。

## 在线预览
以 nginx + uwsgi 进行部署，未做移动端适配。

[link](http://119.28.134.202/signup)

测试账号:

username: test@test.com

password: asd123
## 运行方式

First, clone the repo and install the dependencies.

```bash
$ https://github.com/Caoyiii/django-vue-blog.git
# django dependencies.
$ cd django-vue-blog/backend/
$ pip install -r requirements.txt
# vue dependencies.
$ cd ../frontend/
$ npm i
```
Then, run it.
```bash
# in frontend
$ npm run dev
# in backend
$ python manage.py makemigrations Blog BlogUser
$ python manage.py migrate
# creating an admin user
$ python createsuperuser
...
$ python manage.py runserver
```

Now, open a Web browser and go to "http://localhost:8000/admin/" create posts.

go to "http://localhost:3000/" view.

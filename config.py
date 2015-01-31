#coding:utf-8
import os
from official import app
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SECRET_KEY'] = 'test_site'  ##不加这句时使用flask-admin的网页删除功能时出错出错
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['DATABASE_FILE'] = os.path.join(basedir, 'myofficial.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
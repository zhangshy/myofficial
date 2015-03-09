#coding:utf-8
from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.principal import Principal

from config import SECRET_KEY, SQLALCHEMY_DATABASE_URI
from models import db
from userView import user_view
from blogView import blog_view


USER_ALL = 'user_all'
ROLE_ALL = 'role_all'
USER_PAGE_ALL = 'user_page_all'
EDIT_SELF_PAGE = 'edit_self_page'
EDIT_ALL_PAGE = 'edit_all_page'


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
Principal(app)

app.register_blueprint(user_view)
app.register_blueprint(blog_view)


import official.myAdmin
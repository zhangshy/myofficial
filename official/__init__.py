#coding:utf-8
from flask import Flask
from flask.ext.login import LoginManager, current_user
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.principal import Principal, identity_loaded, RoleNeed, UserNeed, Permission

USER_ALL = 'user_all'
USER_PAGE_ALL = 'user_page_all'
EDIT_SELF_PAGE = 'edit_self_page'
EDIT_ALL_PAGE = 'edit_all_page'


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
Principal(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    print('on_identity_loaded called')
    identity.user = current_user

    if hasattr(current_user, 'id'):
        print('current user has id')
        print(current_user.id)
        identity.provides.add(UserNeed(current_user.id))

    if hasattr(current_user, 'role'):
        print('test')

import official.views
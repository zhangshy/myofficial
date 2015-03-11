#coding:utf-8
import os
from flask import url_for, redirect, current_app, session, flash
import random
from flask.ext.admin import AdminIndexView, expose, form
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext import login
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.datastructures import FileStorage
from sqlalchemy.event import listens_for
import mistune #解析markdown文件
from forms import LoginForm
from flask.ext.principal import Identity, AnonymousIdentity, identity_changed, Permission, RoleNeed
from official import USER_ALL, ROLE_ALL
from models import Blog

#上传文件存放路径
file_path = os.path.join(os.path.dirname(__file__), 'blog/md')
html_path = os.path.join(os.path.dirname(__file__), 'blog/html')
try:
    os.mkdir(file_path)
except OSError:
    pass

try:
    os.mkdir(html_path)
except OSError:
    pass

class MyAdminIndexView(AdminIndexView):
    @expose('/verificationcode')
    def verification_code(self):
        str = ""
        for i in range(5):
            str += random.choice('0123456789abcdefghijklmnopqrstuvwxyz')
        session['verification'] = str
        return str

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated():
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        form = LoginForm()
        if form.validate_on_submit():
            if 'verification' in session and session['verification']==form.verification.data:
                user = form.get_user()
                if check_password_hash(user.password, form.password.data):
                    login.login_user(user)
                    identity_changed.send(current_app._get_current_object(),
                                          identity=Identity(user.id))
                else:
                    print('form in:%s' % form.password.data)
                    flash(u'密码错误')
            else:
                print('verification error:%s' % (form.verification.data))
                flash(u'验证码错误')
        if login.current_user.is_authenticated():
            return redirect(url_for('.index'))
        self._template_args['form'] = form
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        for key in ('identity.name', 'identity.auth_type'):
            session.pop(key, None)

        identity_changed.send(current_app._get_current_object(),
                              identity=AnonymousIdentity())
        return redirect(url_for('.index'))

class MyModelView(ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated()
class UserModelView(ModelView):
    def is_accessible(self):
        return Permission(RoleNeed(USER_ALL)).can()
class RoleModelView(ModelView):
    def is_accessible(self):
        return Permission(RoleNeed(ROLE_ALL)).can()

# Delete hooks for models, delete blogs if models are getting deleted
@listens_for(Blog, 'after_delete')
def del_blog(mapper, connection, target):
    if target.path:
        try:
            os.remove(os.path.join(file_path, target.path))
        except OSError:
            pass
        try:
            os.remove(os.path.join(html_path, os.path.splitext(target.path)[0]+'.html'))
        except OSError:
            pass

'''
修改form.FileUploadField的_save_file方法，在保存文件时将上传的md文件也转成html文件，并将html文件存入../html中
'''
class MyBlogUploadField(form.FileUploadField):
    def _save_file(self, data, filename):
        path = self._get_path(filename)#.../md/file.md
        path = os.path.dirname(path)#../md/
        path = os.path.join(os.path.dirname(path), 'html')#../html/
        if not os.path.exists(path):
            os.makedirs(path, self.permission | 0o111)
        path = os.path.join(path, filename)
        out = "<head><meta charset='utf-8'></head>"
        out += mistune.markdown(data.read())
        with open(os.path.splitext(path)[0]+'.html', 'w') as fo:
            fo.write(out)
        return super(MyBlogUploadField, self)._save_file(data, filename)

class BlogView(ModelView):
    # Override form field to Flask-Admin FileUploadField
    form_overrides = {
        'path': MyBlogUploadField
    }

    # Pass additional parameters to 'path' to FileUploadField constructor
    form_args = {
        'path': {
            'label': 'File',
            'base_path': file_path
        }
    }

    def validate_form(self, form):
        if isinstance(form.path.data, FileStorage):
            if "text/markdown"!=form.path.data.mimetype:
                return False
        return super(BlogView, self).validate_form(form)

    def is_accessible(self):
        return Permission(RoleNeed(ROLE_ALL)).can()

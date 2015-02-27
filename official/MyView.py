#coding:utf-8
from flask import url_for, redirect, current_app, session, flash
import random
from flask.ext.admin import AdminIndexView, expose
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext import login
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm
from flask.ext.principal import Identity, AnonymousIdentity, identity_changed, Permission, RoleNeed
from official import USER_ALL, ROLE_ALL

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

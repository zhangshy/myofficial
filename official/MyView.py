from flask import url_for,redirect
from flask.ext.admin import AdminIndexView, expose
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext import login
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        print('this is /')
        if not login.current_user.is_authenticated():
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        form = LoginForm()
        if form.validate_on_submit():
            user = form.get_user()
            if check_password_hash(user.password, form.password.data):
                login.login_user(user)
            else:
                print('form in:%s' % form.password.data)
        if login.current_user.is_authenticated():
            return redirect(url_for('.index'))
        self._template_args['form'] = form
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))

class MyModelView(ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated()

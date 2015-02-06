#coding: utf-8
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, validators
from config import db
from models import User

class LoginForm(Form):
    name = StringField(u'用户名', validators=[validators.DataRequired()])
    password = PasswordField(u'密码', validators=[validators.DataRequired()])
    verification = StringField(u'验证码', validators=[validators.DataRequired()])

    def get_user(self):
        return db.session.query(User).filter_by(name=self.name.data).first()

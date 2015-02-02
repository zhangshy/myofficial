from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, validators
from config import db
from models import User

class LoginForm(Form):
    name = StringField(validators=[validators.required()])
    password =PasswordField(validators=[validators.required()])

    def get_user(self):
        return db.session.query(User).filter_by(name=self.name.data).first()

'''
crate test database
'''
import getpass

from flask.ext.sqlalchemy import SQLAlchemy
from official import app
from werkzeug.security import generate_password_hash
from official.models import User


def create_user():
    name = raw_input('user name:')
    email = raw_input('enter email:')
    role_id = raw_input('enter role_id:')
    password = getpass.getpass('enter password:')
    tmp = getpass.getpass('enter password again:')
    if password!=tmp:
        print('password not equal')
        return
    db = SQLAlchemy(app)
    user = User()
    user.init(name, email, role_id, generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return


if __name__ == '__main__':
        create_user()
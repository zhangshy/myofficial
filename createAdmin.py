'''
crate test database
'''
import os
from werkzeug.security import generate_password_hash
import getpass
from official import db
from official.views import User
from config import app

def create_admin():
    name = raw_input('user name:')
    email = raw_input('enter email:')
    password = getpass.getpass('enter password:')
    tmp = getpass.getpass('enter password again:')
    if password!=tmp:
        print('password not equal')
        return
    user = User(name, email, generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return


if __name__ == '__main__':
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])
    print(database_path)
    if os.path.exists(database_path):
        create_admin()
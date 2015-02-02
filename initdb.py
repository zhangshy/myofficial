'''
crate test database
'''
import os
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
import getpass
from official import app
from config import db
from official.views import Stb, User

def build_sample_db():
    name = raw_input('user name:')
    email = raw_input('enter email:')
    password = getpass.getpass('enter password:')
    tmp = getpass.getpass('enter password again:')
    if password!=tmp:
        print('password not equal')
        return
    db.drop_all()
    db.create_all()
    user = User(name, email, generate_password_hash(password))
    stb1 = Stb('T2', 'http://img.tvhome.com/uploads/2014/09/10/19290aff2d718cbed9265f0266b64bc7.jpg',
               260.0, 'http://www.taixin.cn', 'taixin', 'DVB+OTT', datetime.utcnow()+timedelta(hours=1))
    stb2 = Stb('X1', 'http://www.taixin.cn/uploadfiles/image/20141226/20141226132514_6076.jpg',
               399.0, 'http://www.taixin.cn', 'taixin', 'DVB+OTT', datetime.utcnow()+timedelta(hours=2, minutes=30))
    stb3 = Stb('X2', 'http://www.taixin.cn/uploadfiles/image/20141226/20141226132646_0860.jpg',
               299.0, 'http://www.taixin.cn', 'taixin', 'DVB+OTT', datetime.utcnow()+timedelta(hours=1, minutes=40))
    db.session.add(stb1)
    db.session.add(stb2)
    db.session.add(stb3)
    db.session.add(user)
    db.session.commit()
    return


if __name__ == '__main__':
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])
    print(database_path)
    if not os.path.exists(database_path):
        build_sample_db()
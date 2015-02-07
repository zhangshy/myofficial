from datetime import datetime
import random

from flask import render_template, url_for, redirect
from flask.ext.admin import Admin

from official import db, login_manager
from config import app
from models import Stb, User
from MyView import MyAdminIndexView, MyModelView


#admin = Admin(app, index_view=MyAdminIndexView())
#admin.add_view(ModelView(Stb, db.session))
admin = Admin(app, 'mySite', index_view=MyAdminIndexView(), base_template='my_master.html')
admin.add_view(MyModelView(Stb, db.session))

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)

@app.route('/')
def index():
    return redirect(url_for('stb'))

@app.route('/stb')
def stb():
    stbs = Stb.query.all()
    for stb in stbs:
        tmp = stb.end_time - datetime.utcnow()
#        stb.leftTime = tmp.total_seconds()
        stb.leftTime = tmp.days*86400 + tmp.seconds
        print("leftTime: %d" % (stb.leftTime))
    return render_template('stb.html', stbs=stbs)

@app.route('/verificationcode')
def verification_code():
    str = ""
    for i in range(5):
        str += random.choice('0123456789abcdefghijklmnopqrstuvwxyz')
    return str

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/bootstrap/<name>')
def bootstrap_test1(name):
    return render_template('bootstrap_'+name+'.html')

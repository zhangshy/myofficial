#coding: utf-8
from datetime import datetime
import random

from flask import render_template, url_for, redirect
from flask.ext.admin import Admin

from official import db, login_manager
from config import app
from models import Stb, User, Role
from MyView import MyAdminIndexView, MyModelView, UserModelView, RoleModelView


#admin = Admin(app, index_view=MyAdminIndexView())
#admin.add_view(ModelView(Stb, db.session))
admin = Admin(app, 'mySite', index_view=MyAdminIndexView(), base_template='my_master.html')
admin.add_view(UserModelView(User, db.session))
admin.add_view(RoleModelView(Role, db.session))
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

@app.route('/page/<name>')
def user_page(name):
    body = {
            'images':[
                {'src':'http://ww4.sinaimg.cn/bmiddle/62e2b033jw1ep0vete9q5j20xc18gwlh.jpg', 'alt':u'雅少', 'title':u'雅少', 'desc':u'美美哒'},
                {'src':'http://ww4.sinaimg.cn/bmiddle/62e2b033jw1eozxedhe7uj20dc0hsjtl.jpg', 'alt':u'雅少', 'title':u'雅少', 'desc':u'美美哒'},
                {'src':'http://ww4.sinaimg.cn/bmiddle/62e2b033gw1eon5mayp73j20qs0qs0xk.jpg', 'alt':u'雅少', 'title':u'雅少', 'desc':u'美美哒'},
            ],
            'weibo':{
                'avatar': 'http://tp4.sinaimg.cn/1659023411/180/40058975018/0',
                'href': 'http://weibo.com/910317000',
                'alt': u'雅少新浪微博'
            },
            'zhibo':{
                'avatar': 'http://www.huomaotv.com/uc_server/avatar.php?uid=100&size=small',
                'href': 'http://www.huomaotv.com/live/15',
                'alt': u'雅少火猫直播'
            }
        }
    return render_template('userpage.html', body=body, title=u'雅少萌萌哒')


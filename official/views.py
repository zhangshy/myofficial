from flask import render_template
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from datetime import datetime
from config import db
from models import Stb
from official import app
from MyView import MyView


admin = Admin(app)
admin.add_view(ModelView(Stb, db.session))

@app.route('/')
def index():
    '''
    stbs = [
        {
            'name': 'T2',
            'img': 'http://img.tvhome.com/uploads/2014/09/10/19290aff2d718cbed9265f0266b64bc7.jpg',
            'price': 260.0,
            'href': 'http://www.taixin.cn',
            'promsg_title': 'taixin',
            'promsg_desc': 'DVB+OTT',
            'left_time': 84840,
        },
        {
            'name': 'X1',
            'img': 'http://www.taixin.cn/uploadfiles/image/20141226/20141226132514_6076.jpg',
            'price': 399.0,
            'href': "http://www.taixin.cn",
            'promsg_title': 'taixin',
            'promsg_desc': 'DVB+OTT',
            'left_time': 74842,
        },
        {
            'name': 'X2',
            'img': 'http://www.taixin.cn/uploadfiles/image/20141226/20141226132646_0860.jpg',
            'price': 299.0,
            'href': "http://www.taixin.cn",
            'promsg_title': 'taixin',
            'promsg_desc': 'DVB+OTT',
            'left_time': 74842,
        },
    ]
    '''
    stbs = Stb.query.all()
    for stb in stbs:
        tmp = stb.end_time - datetime.utcnow()
        stb.leftTime = tmp.total_seconds()
        print("leftTime: %d" % (stb.leftTime))
    return render_template('index.html', stbs=stbs)

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/bootstrap/<name>')
def bootstrap_test1(name):
    return render_template('bootstrap_'+name+'.html')

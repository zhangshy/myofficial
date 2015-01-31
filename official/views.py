from flask import render_template
from flask.ext.admin import Admin
from config import db
from official import app
from MyView import MyView

class Stb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)
    img = db.Column(db.String(120))
    price = db.Column(db.Float)
    href = db.Column(db.String(120))
    title = db.Column(db.String(40))
    desc = db.Column(db.String(240))
    end_time = db.Column(db.Integer)

    def __init__(self, name, img, price, href, title, desc, end_time):
        self.name = name
        self.img = img
        self.price = price
        self.href = href
        self.title = title
        self.desc = desc
        self.end_time = end_time

    def __repr__(self):
        return '<Stb %r>' % self.name

admin = Admin(app)
admin.add_view(MyView(name='Hello 1', endpoint='test1', category='Test'))
admin.add_view(MyView(name='Hello 2', endpoint='test2', category='Test'))
admin.add_view(MyView(name='Hello 3', endpoint='test3', category='Test'))

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
    return render_template('index.html', stbs=stbs)

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/bootstrap/<name>')
def bootstrap_test1(name):
    return render_template('bootstrap_'+name+'.html')

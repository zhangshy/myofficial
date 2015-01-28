from flask import render_template
from flask.ext.admin import Admin
from official import app, db
from MyView import MyView

class Stb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)
    img = db.Column(db.String(120), unique=True)
    price = db.Column(db.Float, unique=True)

    def __init__(self, name, img, price):
        self.name = name
        self.img = img
        self.price = price

    def __repr__(self):
        return '<Stb %r>' % self.name

admin = Admin(app)
admin.add_view(MyView(name='Hello 1', endpoint='test1', category='Test'))
admin.add_view(MyView(name='Hello 2', endpoint='test2', category='Test'))
admin.add_view(MyView(name='Hello 3', endpoint='test3', category='Test'))

@app.route('/')
def index():
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
    return render_template('index.html', stbs=stbs)

@app.route('/test')
def test():
    return render_template('test.html')

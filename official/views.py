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
            'name': 'X1',
            'img': 'http://www.taixin.cn/uploadfiles/image/20141226/20141226132514_6076.jpg',
            'price': 399,
            'href': "http://www.taixin.cn",
        },
        {
            'name': 'X2',
            'img': 'http://www.taixin.cn/uploadfiles/image/20141226/20141226132646_0860.jpg',
            'price': 299,
            'href': "http://www.taixin.cn",
        },
    ]
    return render_template('index.html', stbs=stbs)
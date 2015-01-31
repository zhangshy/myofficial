from config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    email = db.Column(db.Unicode(64))

    def __unicode__(self):
        return self.name


class Stb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)
    img = db.Column(db.String(120))
    price = db.Column(db.Float)
    href = db.Column(db.String(120))
    title = db.Column(db.String(40))
    desc = db.Column(db.String(240))
    end_time = db.Column(db.DateTime)

    def __init__(self, name=None, img=None, price=None, href=None, title=None, desc=None, end_time=None):
        self.name = name
        self.img = img
        self.price = price
        self.href = href
        self.title = title
        self.desc = desc
        self.end_time = end_time

    def __repr__(self):
        return '<Stb %r>' % self.name
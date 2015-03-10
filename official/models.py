#coding:utf-8
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()
'''
用户表
'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.String(32))
    role = db.relationship('Role', backref='user', lazy='dynamic')

    def init(self, name, email, role_id, password):
        self.name = name
        self.email = email
        self.role_id = role_id
        self.password = password
    '''
    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password
    '''
    def __unicode__(self):
        return self.name

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.id

'''
测试表
'''
class Stb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)
    img = db.Column(db.String(120))
    price = db.Column(db.Float)
    href = db.Column(db.String(120))
    title = db.Column(db.String(40))
    desc = db.Column(db.String(240))
    end_time = db.Column(db.DateTime)
    '''
    def __init__(self, name=None, img=None, price=None, href=None, title=None, desc=None, end_time=None):
        self.name = name
        self.img = img
        self.price = price
        self.href = href
        self.title = title
        self.desc = desc
        self.end_time = end_time
    '''
    def __repr__(self):
        return '<Stb %r>' % self.name

'''
权限表
'''
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    permission = db.Column(db.String(16))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return self.permission

'''
展示用户
'''
class PeopleShow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))
    nickname = db.Column(db.String(16))
    title = db.Column(db.String(64))
    desc = db.Column(db.String(256))
    weibo_follow = db.Column(db.String(128))
    weibo_avatar = db.Column(db.String(128))
    weibo_href = db.Column(db.String(128))
    weibo_desc = db.Column(db.String(64))
    live_avatar = db.Column(db.String(128))
    live_href = db.Column(db.String(128))
    live_alt = db.Column(db.String(64))
    live_src = db.Column(db.String(64))
    images = db.Column(db.String(512))
    image_vote = db.relationship('ImageVote', backref='people_show', lazy='dynamic')
    weibo = db.relationship('Weibo', backref='people_show', lazy='dynamic')
    list_image = db.relationship('ListImage', backref='people_show', lazy='dynamic')
    def __repr__(self):
        return self.name

'''
投票活动
'''
class VoteEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    description = db.Column(db.String(256))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    result = db.Column(db.String(128))
    image_vote = db.relationship('ImageVote', backref='vote_event', lazy='dynamic')

'''
可用于投票的image
'''
class ImageVote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    src = db.Column(db.String(128))
    description = db.Column(db.String(128))
    votes = db.Column(db.Integer, default=0)
    event_id = db.Column(db.Integer, db.ForeignKey('vote_event.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('people_show.id'))

'''
发布文章
'''
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sticky = db.Column(db.Boolean, default=False)
    title = db.Column(db.String(64))
    summary = db.Column(db.String(256))
    images = db.Column(db.String(512))
    youku_vid = db.Column(db.String(20))
    href = db.Column(db.String(128))
    body = db.Column(db.Text)

'''
微博链接
'''
class Weibo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300))
    images = db.Column(db.String(512))
    href = db.Column(db.String(128))
    people_id = db.Column(db.Integer, db.ForeignKey('people_show.id'))

'''
图片墙
'''
class ListImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    src = db.Column(db.String(80))
    href = db.Column(db.String(128))
    content = db.Column(db.String(300))
    people_id = db.Column(db.Integer, db.ForeignKey('people_show.id'))

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    path = db.Column(db.String(128))
    desc = db.Column(db.String(128))

    def __unicode__(self):
        return self.name

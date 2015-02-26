#coding: utf-8
from datetime import datetime
import random

from flask import render_template, url_for, redirect, request, Blueprint
import mistune
from official.models import db, Stb, ImageVote, Post, PeopleShow, Weibo, ListImage
from config import YOUKU_CLIENT_ID

user_view = Blueprint("user_view", __name__, template_folder="templates", static_folder="static")

@user_view.route('/')
def index():
    return user_page('yaya')
    #return redirect(url_for('.user_page', name='yaya'))

@user_view.route('/stb')
def stb():
    stbs = Stb.query.all()
    for stb in stbs:
        tmp = stb.end_time - datetime.utcnow()
#        stb.leftTime = tmp.total_seconds()
        stb.leftTime = tmp.days*86400 + tmp.seconds
        print("leftTime: %d" % (stb.leftTime))
    return render_template('stb.html', stbs=stbs)

@user_view.route('/verificationcode')
def verification_code():
    str = ""
    for i in range(5):
        str += random.choice('0123456789abcdefghijklmnopqrstuvwxyz')
    return str

@user_view.route('/test')
def test():
    #return render_template('test.html')
    return redirect(url_for('.post_of_id', id=1))

@user_view.route('/bootstrap/<name>')
def bootstrap_test1(name):
    return render_template('bootstrap_'+name+'.html')

@user_view.route('/page/<name>')
def user_page(name):
    #people = PeopleShow.query.filter_by(name=name).first()
    peoples = PeopleShow.query.filter_by(name=name).all()
    people = peoples[0]
    if people==None:
        print('people is none')
        return "not exist"
    lImages = people.images.split(';')
    sticky = Post.query.filter_by(sticky=True).first()
    weibo = Weibo.query.filter_by(people_id=people.id).first()
    return render_template('user_page.html', people=people, lImages=lImages, sticky_post=sticky, client_id=YOUKU_CLIENT_ID,
                weibo=weibo, title=people.title, peoples=peoples)

@user_view.route('/vote/img', methods=['POST', 'GET'])
def vote_image():
    if request.method == 'GET':
        id = request.args.get('id', -1)
        votes = ImageVote.query.filter_by(id=id).first().votes
        votes+=1
        ImageVote.query.filter_by(id=id).first().votes = votes
        db.session.commit()
        return str(votes)

@user_view.route('/post/<id>')
def post_of_id(id):
    post = Post.query.filter_by(id=id).first()
    if post==None:
        print("in posts %s is null" % id)
        return "Not exist"
    return render_template('post_page.html', post=post, body=mistune.markdown(post.body), title=post.title, client_id=YOUKU_CLIENT_ID)

@user_view.route('/image/<name>')
def list_images(name):
    #people = PeopleShow.query.filter_by(name=name).first()
    peoples = PeopleShow.query.filter_by(name=name).all()
    people = peoples[0]
    if people==None:
        print('list_images %s not exist' % name)
        return 'Not exist'
    id = people.id
    images = ListImage.query.filter_by(people_id=id).all()
    return render_template('list_image.html', images=images, title=u'雅雅美图', people=people, peoples=peoples)


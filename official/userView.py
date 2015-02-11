#coding: utf-8
from datetime import datetime
import random

from flask import render_template, url_for, redirect, request, Blueprint

from official.models import Stb, User, Role, ImageVote, ImageCarousel, UserReferPage, db
from getData import getDataFromDB

user_view = Blueprint("user_view", __name__, template_folder="templates", static_folder="static")

@user_view.route('/')
def index():
    return redirect(url_for('.user_page', name='yaya'))

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
    return render_template('test.html')

@user_view.route('/bootstrap/<name>')
def bootstrap_test1(name):
    return render_template('bootstrap_'+name+'.html')

@user_view.route('/page/<name>')
def user_page(name):
    '''
    body = {
            'images':[
                {'src':'http://ww4.sinaimg.cn/bmiddle/62e2b033jw1ep0vete9q5j20xc18gwlh.jpg', 'alt':u'雅少', 'title':u'雅少', 'desc':u'美美哒'},
                {'src':'http://ww4.sinaimg.cn/bmiddle/62e2b033jw1eozxedhe7uj20dc0hsjtl.jpg', 'alt':u'雅少', 'title':u'雅少', 'desc':u'美美哒'},
                {'src':'http://ww4.sinaimg.cn/bmiddle/62e2b033gw1eon5mayp73j20qs0qs0xk.jpg', 'alt':u'雅少', 'title':u'雅少', 'desc':u'美美哒'},
            ],
            'weibo':{
                'avatar': 'http://tp4.sinaimg.cn/1659023411/180/40058975018/0',
                'href': 'http://weibo.com/910317000',
                'alt': u'NewBeeTV_雅雅的新浪微博'
            },
            'zhibo':{
                'avatar': 'http://www.huomaotv.com/uc_server/avatar.php?uid=100&size=small',
                'href': 'http://www.huomaotv.com/live/15',
                'alt': u'雅少的火猫直播'
            },
            'vImages':[
                {'src':'http://ww4.sinaimg.cn/bmiddle/62e2b033gw1eoh3k0pd44j20qs0zq7av.jpg', 'votes':0, 'id':0},
                {'src':'http://ww1.sinaimg.cn/bmiddle/62e2b033jw1eojjmxcspfj20qo0zkahn.jpg', 'votes':0, 'id':1},
                {'src':'http://ww4.sinaimg.cn/bmiddle/005vDrjogw1eokru36yixj30dc0k0aan.jpg', 'votes':0, 'id':2},
            ],
        }
    '''
    body = getDataFromDB(name)
    return render_template('userpage.html', body=body, title=u'NewBeeTV_雅雅')

@user_view.route('/vote/img', methods=['POST', 'GET'])
def vote_image():
    if request.method == 'GET':
        id = request.args.get('id', -1)
        votes = ImageVote.query.filter_by(id=id).first().votes
        votes+=1
        ImageVote.query.filter_by(id=id).first().votes = votes
        db.session.commit()
        #return datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return str(votes)

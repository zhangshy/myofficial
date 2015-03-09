#coding: utf-8
import os
from flask import Blueprint, render_template, redirect, url_for
from models import PeopleShow

blog_view = Blueprint("blog_view", __name__, template_folder="templates", static_folder="static")

@blog_view.route('/')
def index():
    return redirect(url_for('.list'))
    #return redirect(url_for('.blog', name='pandas_select'))

@blog_view.route('/blog')
def list():
    peoples = PeopleShow.query.all()
    basedir = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(basedir, 'blog')
    files = os.listdir(path)
    lists = [os.path.splitext(f)[0] for f in files]
    return render_template('blog_page.html', title=u'pandas学习', peoples=peoples, lists=lists)

@blog_view.route('/blog/<name>')
def blog(name):
    peoples = PeopleShow.query.all()
    return render_template('blog_page.html', title=u'pandas学习', peoples=peoples, file=name)

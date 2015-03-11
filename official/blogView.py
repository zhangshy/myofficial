#coding: utf-8
import os
from flask import Blueprint, render_template, redirect, url_for
from models import PeopleShow, Blog, BlogCategory

blog_view = Blueprint("blog_view", __name__, template_folder="templates", static_folder="static")

@blog_view.route('/')
def index():
    return redirect(url_for('.list'))
    #return redirect(url_for('.blog', name='pandas_select'))

@blog_view.route('/blog')
def list():
    peoples = PeopleShow.query.all()
    lists = Blog.query.all()
    return render_template('blog_page.html', title=u'blog列表', peoples=peoples, lists=lists)

@blog_view.route('/blog/<name>')
def blog(name):
    peoples = PeopleShow.query.all()
    blog = Blog.query.filter_by(name=name).first()
    title = u"文章不存在"
    if blog!=None:
        title = BlogCategory.query.filter_by(id=blog.category).first().name
    return render_template('blog_page.html', title=title, peoples=peoples, blog=name)

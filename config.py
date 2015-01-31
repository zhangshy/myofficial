import os
from official import app
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['DATABASE_FILE'] = os.path.join(basedir, 'myofficial.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
db = SQLAlchemy(app)
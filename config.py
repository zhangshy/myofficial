#coding:utf-8

SECRET_KEY = 'test_site'  ##不加这句时使用flask-admin的网页删除功能时出错出错
#basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['DATABASE_FILE'] = os.path.join(basedir, 'myofficial.db')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
#app.config['SQLALCHEMY_ECHO'] = True
SQLALCHEMY_DATABASE_URI = 'mysql://zsy:test@localhost/myofficial'
YOUKU_CLIENT_ID = '6ad18b14f6a41ed9'







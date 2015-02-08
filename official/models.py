from official import app, db
from flask.ext.login import current_user
from flask.ext.principal import identity_loaded, RoleNeed, UserNeed, Permission

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

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    permission = db.Column(db.String(16))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return self.permission

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = current_user

    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))

    if hasattr(current_user, 'role'):
#        roles = Role.query.all()
        roles = Role.query.filter_by(user_id=current_user.get_id())
        for role in roles:
            identity.provides.add(RoleNeed(role.permission))

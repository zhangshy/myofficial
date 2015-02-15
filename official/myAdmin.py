from flask.ext.admin import Admin
from flask.ext.login import current_user
from flask.ext.principal import identity_loaded, RoleNeed, UserNeed, Permission
from official import app, db, login_manager
from MyView import MyAdminIndexView, MyModelView, UserModelView, RoleModelView
from models import Stb, User, Role, PeopleShow, VoteEvent, ImageVote, Post, Weibo, ListImage


#admin = Admin(app, index_view=MyAdminIndexView())
#admin.add_view(ModelView(Stb, db.session))
admin = Admin(app, 'mySite', index_view=MyAdminIndexView(), base_template='my_master.html')
admin.add_view(UserModelView(User, db.session))
admin.add_view(RoleModelView(Role, db.session))
admin.add_view(RoleModelView(PeopleShow, db.session))
admin.add_view(RoleModelView(VoteEvent, db.session))
admin.add_view(RoleModelView(ImageVote, db.session))
admin.add_view(RoleModelView(Post, db.session))
admin.add_view(RoleModelView(Weibo, db.session))
admin.add_view(RoleModelView(ListImage, db.session))
#admin.add_view(MyModelView(Stb, db.session))


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


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)
"""init migration

Revision ID: c01a3266eae
Revises: None
Create Date: 2015-02-14 00:13:30.666275

"""

# revision identifiers, used by Alembic.
revision = 'c01a3266eae'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('summary', sa.String(length=256), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stb',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('img', sa.String(length=120), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('href', sa.String(length=120), nullable=True),
    sa.Column('title', sa.String(length=40), nullable=True),
    sa.Column('desc', sa.String(length=240), nullable=True),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('people_show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=16), nullable=True),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('desc', sa.String(length=256), nullable=True),
    sa.Column('weibo_avatar', sa.String(length=128), nullable=True),
    sa.Column('weibo_href', sa.String(length=128), nullable=True),
    sa.Column('weibo_desc', sa.String(length=64), nullable=True),
    sa.Column('live_avatar', sa.String(length=128), nullable=True),
    sa.Column('live_href', sa.String(length=128), nullable=True),
    sa.Column('live_alt', sa.String(length=64), nullable=True),
    sa.Column('images', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('role_id', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_table('vote_event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.Column('result', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('image_vote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('src', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.Column('votes', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('people_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['vote_event.id'], ),
    sa.ForeignKeyConstraint(['people_id'], ['people_show.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('permission', sa.String(length=16), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('role')
    op.drop_table('image_vote')
    op.drop_table('vote_event')
    op.drop_table('user')
    op.drop_table('people_show')
    op.drop_table('stb')
    op.drop_table('post')
    ### end Alembic commands ###
"""init migration

Revision ID: 419ce474709e
Revises: None
Create Date: 2015-02-09 23:48:57.679037

"""

# revision identifiers, used by Alembic.
revision = '419ce474709e'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
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
    op.drop_table('stb')
    op.drop_table('user')
    ### end Alembic commands ###
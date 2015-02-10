"""empty message

Revision ID: 474e2bb65507
Revises: 419ce474709e
Create Date: 2015-02-11 00:34:15.308490

"""

# revision identifiers, used by Alembic.
revision = '474e2bb65507'
down_revision = '419ce474709e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image_carousel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('src', sa.String(length=128), nullable=True),
    sa.Column('alt', sa.String(length=128), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('desc', sa.String(length=256), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('image_vote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('src', sa.String(length=128), nullable=True),
    sa.Column('votes', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_refer_page',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('avatar', sa.String(length=128), nullable=True),
    sa.Column('href', sa.String(length=128), nullable=True),
    sa.Column('alt', sa.String(length=256), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_refer_page')
    op.drop_table('image_vote')
    op.drop_table('image_carousel')
    ### end Alembic commands ###

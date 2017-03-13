"""empty message

Revision ID: 054170757fbb
Revises: 
Create Date: 2017-03-13 06:32:19.972506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '054170757fbb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('userid', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(length=1), nullable=True),
    sa.Column('biography', sa.Text(), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('created_on', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('userid'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    # ### end Alembic commands ###

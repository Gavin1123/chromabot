"""Added display_end to Battle

Revision ID: 41fe909190d3
Revises: 2e37930ecb54
Create Date: 2013-09-16 18:47:44.229667

"""

# revision identifiers, used by Alembic.
revision = '41fe909190d3'
down_revision = '2e37930ecb54'

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    eval("upgrade_%s" % engine_name)()


def downgrade(engine_name):
    eval("downgrade_%s" % engine_name)()





def upgrade_engine1():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('battles', sa.Column('display_ends', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade_engine1():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('battles', 'display_ends')
    ### end Alembic commands ###


def upgrade_engine2():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('battles', sa.Column('display_ends', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade_engine2():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('battles', 'display_ends')
    ### end Alembic commands ###


def upgrade_engine3():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('battles', sa.Column('display_ends', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade_engine3():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('battles', 'display_ends')
    ### end Alembic commands ###


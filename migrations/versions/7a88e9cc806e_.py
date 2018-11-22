"""empty message

Revision ID: 7a88e9cc806e
Revises: 92ea7ef106c3
Create Date: 2018-10-27 12:51:51.562573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a88e9cc806e'
down_revision = '92ea7ef106c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_log_user_id', table_name='log')
    op.create_index(op.f('ix_log_user_id'), 'log', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_log_user_id'), table_name='log')
    op.create_index('ix_log_user_id', 'log', ['user_id'], unique=True)
    # ### end Alembic commands ###
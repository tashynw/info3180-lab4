"""empty message

Revision ID: 392906488485
Revises: 4caf17b6e0fa
Create Date: 2024-03-06 15:24:55.444148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '392906488485'
down_revision = '4caf17b6e0fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=128), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###

"""empty message

Revision ID: 5e6420cb8dd0
Revises: 79600146a797
Create Date: 2020-11-01 16:46:42.522859

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5e6420cb8dd0'
down_revision = '79600146a797'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('goods', 'price',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('goods', 'price',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
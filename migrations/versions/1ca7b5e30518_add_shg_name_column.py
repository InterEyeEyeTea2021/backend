"""Add SHG_Name column

Revision ID: 1ca7b5e30518
Revises: b712437000e6
Create Date: 2021-03-16 03:37:43.965907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ca7b5e30518'
down_revision = 'b712437000e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_shg', sa.Column('SHG_Name', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_shg', 'SHG_Name')
    # ### end Alembic commands ###

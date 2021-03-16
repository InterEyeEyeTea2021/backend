"""Final schema

Revision ID: 859da35cea70
Revises: 1ca7b5e30518
Create Date: 2021-03-16 15:25:22.858718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '859da35cea70'
down_revision = '1ca7b5e30518'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('bid', sa.Column(
        'tender_id', sa.Integer, nullable=True))
    op.create_foreign_key(
            "bid_tender_id_fkey", "bid",
            "tender", ["tender_id"], ["id"])


def downgrade():
    pass

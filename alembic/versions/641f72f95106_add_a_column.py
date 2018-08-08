"""Add a column

Revision ID: 641f72f95106
Revises: 31e00c6ce082
Create Date: 2018-08-08 17:08:58.536565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '641f72f95106'
down_revision = '31e00c6ce082'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))


def downgrade():
    op.drop_column('account', 'last_transaction_date')

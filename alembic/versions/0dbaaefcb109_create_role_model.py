"""Create Role model

Revision ID: 0dbaaefcb109
Revises: fa515fcb7985
Create Date: 2018-08-17 14:21:50.926240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0dbaaefcb109'
down_revision = 'fa515fcb7985'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('role',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('role')

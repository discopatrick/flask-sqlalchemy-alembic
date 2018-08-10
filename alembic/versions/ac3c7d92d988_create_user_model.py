"""Create User model

Revision ID: ac3c7d92d988
Revises:
Create Date: 2018-08-10 09:20:42.419702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac3c7d92d988'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=True),
        sa.Column('fullname', sa.String(length=50), nullable=True),
        sa.Column('password', sa.String(length=50), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('users')

"""Create Address model

Revision ID: fa515fcb7985
Revises: ac3c7d92d988
Create Date: 2018-08-10 09:50:24.791679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa515fcb7985'
down_revision = 'ac3c7d92d988'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('addresses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email_address', sa.String(length=50), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('addresses')

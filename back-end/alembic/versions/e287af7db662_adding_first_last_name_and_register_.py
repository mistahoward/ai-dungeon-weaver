"""Adding first & last name and register & login date

Revision ID: e287af7db662
Revises: b9869bdd790c
Create Date: 2023-11-25 23:26:05.205915

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e287af7db662'
down_revision: Union[str, None] = 'b9869bdd790c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('user', sa.Column('first_name', sa.String(length=255), nullable=False))
    op.add_column('user', sa.Column('last_name', sa.String(length=255), nullable=False))
    op.add_column('user', sa.Column('register_date', sa.Integer(), nullable=False))
    op.add_column('user', sa.Column('last_login_date', sa.Integer(), nullable=False))

def downgrade() -> None:
    op.drop_column('user', 'last_login_date')
    op.drop_column('user', 'register_date')
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
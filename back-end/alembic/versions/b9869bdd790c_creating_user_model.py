"""Creating User Model

Revision ID: b9869bdd790c
Revises: 
Create Date: 2023-11-25 22:54:43.034099

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9869bdd790c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None: 
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', nullable=False),
        sa.Column('email', nullable=False),
        sa.Column('password', nullable=False),
        sa.Column('salt', nullable=False),
    )

def downgrade() -> None:
    op.drop_table('user')
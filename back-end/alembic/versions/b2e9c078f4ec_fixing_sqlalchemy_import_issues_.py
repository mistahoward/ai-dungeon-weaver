"""Fixing sqlalchemy import issues, therefore fixing alembic

Revision ID: b2e9c078f4ec
Revises: e287af7db662
Create Date: 2023-12-08 22:05:23.403189

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b2e9c078f4ec'
down_revision: Union[str, None] = 'e287af7db662'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user'):
        # op.drop_constraint('user_email_key', type_='unique')
        op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=False)
        op.create_unique_constraint(None, 'user', ['email'])        
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user'):
        op.drop_constraint(None, 'user', type_='unique')
        op.drop_index(op.f('ix_user_email'), table_name='user')
    # ### end Alembic commands ###
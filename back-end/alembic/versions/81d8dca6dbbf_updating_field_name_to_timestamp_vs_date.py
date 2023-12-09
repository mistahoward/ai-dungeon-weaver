"""Updating field name to timestamp vs date

Revision ID: 81d8dca6dbbf
Revises: 7b8986738c92
Create Date: 2023-12-09 11:01:03.508277

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81d8dca6dbbf'
down_revision: Union[str, None] = '7b8986738c92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('authentication_log', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timestamp', sa.Integer(), nullable=False))
        batch_op.drop_column('date')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('authentication_log', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.INTEGER(), nullable=False))
        batch_op.drop_column('timestamp')

    # ### end Alembic commands ###

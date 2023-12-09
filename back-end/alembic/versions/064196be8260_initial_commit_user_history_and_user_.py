"""Initial commit, user history and user table

Revision ID: 064196be8260
Revises: 
Create Date: 2023-12-09 01:09:46.905081

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '064196be8260'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('register_date', sa.Integer(), nullable=False),
    sa.Column('last_login_date', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_id'), ['id'], unique=False)

    op.create_table('user_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('field_name', sa.String(), nullable=True),
    sa.Column('old_value', sa.String(), nullable=True),
    sa.Column('new_value', sa.String(), nullable=True),
    sa.Column('date', sa.Integer(), nullable=False),
    sa.Column('operation', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user_history', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_history_id'), ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_history', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_history_id'))

    op.drop_table('user_history')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_id'))

    op.drop_table('user')
    # ### end Alembic commands ###

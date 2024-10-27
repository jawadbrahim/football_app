"""tokens

Revision ID: 9434c1a1f33f
Revises: bd2662f871a2
Create Date: 2024-10-27 11:46:52.507451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9434c1a1f33f'
down_revision = 'bd2662f871a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('auth', schema=None) as batch_op:
        batch_op.add_column(sa.Column('token_id', sa.UUID(), nullable=True))
        batch_op.create_foreign_key(None, 'token', ['token_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('auth', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('token_id')

    # ### end Alembic commands ###

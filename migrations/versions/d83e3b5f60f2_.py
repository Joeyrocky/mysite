"""empty message

Revision ID: d83e3b5f60f2
Revises: 7ff226557380
Create Date: 2023-08-22 13:28:24.385504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd83e3b5f60f2'
down_revision = '7ff226557380'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ministry', sa.Integer(), nullable=True))
        batch_op.drop_column('indexnumber')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('indexnumber', sa.INTEGER(), nullable=True))
        batch_op.drop_column('ministry')

    # ### end Alembic commands ###

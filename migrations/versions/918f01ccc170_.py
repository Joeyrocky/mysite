"""empty message

Revision ID: 918f01ccc170
Revises: 75da38448eb7
Create Date: 2022-09-05 16:49:23.727433

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '918f01ccc170'
down_revision = '75da38448eb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('Nationality', sa.Integer(), nullable=True))
    op.add_column('person', sa.Column('Marital', sa.String(), nullable=True))
    op.add_column('person', sa.Column('Health', sa.String(), nullable=True))
    op.add_column('person', sa.Column('Extra', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'person', ['lastname'])
    op.drop_column('person', 'name')
    op.drop_column('person', 'picture')
    op.drop_column('person', 'gender')
    op.drop_column('person', 'guardian')
    op.drop_column('person', 'current_place_of_work')
    op.drop_column('person', 'marital_status')
    op.drop_column('person', 'next_of_kin')
    op.drop_column('person', 'health_status')
    op.drop_column('person', 'primary_phone_number')
    op.drop_column('person', 'status_doa')
    op.drop_column('person', 'age')
    op.drop_column('person', 'home_address')
    op.drop_column('person', 'nationality')
    op.drop_column('person', 'extra_curriculum_activities')
    op.drop_column('person', 'brithdate')
    op.drop_column('person', 'secondary_phone_number')
    op.drop_column('person', 'class_designaiton')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('class_designaiton', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('secondary_phone_number', sa.INTEGER(), nullable=True))
    op.add_column('person', sa.Column('brithdate', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('extra_curriculum_activities', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('nationality', sa.VARCHAR(length=100), nullable=True))
    op.add_column('person', sa.Column('home_address', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('age', sa.INTEGER(), nullable=True))
    op.add_column('person', sa.Column('status_doa', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('primary_phone_number', sa.INTEGER(), nullable=True))
    op.add_column('person', sa.Column('health_status', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('next_of_kin', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('marital_status', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('current_place_of_work', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('guardian', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('gender', sa.VARCHAR(length=10), nullable=True))
    op.add_column('person', sa.Column('picture', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('name', sa.VARCHAR(length=200), nullable=True))
    op.drop_constraint(None, 'person', type_='unique')
    op.drop_column('person', 'Extra')
    op.drop_column('person', 'Health')
    op.drop_column('person', 'Marital')
    op.drop_column('person', 'Nationality')
    # ### end Alembic commands ###
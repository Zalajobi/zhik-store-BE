"""Initial migration.

Revision ID: 8085fdc7d7c6
Revises: 
Create Date: 2022-05-01 01:37:52.606978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8085fdc7d7c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('customer', 'title', existing_type=sa.VARCHAR(length=10), nullable=False)
    op.alter_column('customer', 'first_name', existing_type=sa.VARCHAR(length=60), nullable=False)
    op.alter_column('customer', 'last_name', existing_type=sa.VARCHAR(length=60), nullable=False)
    op.alter_column('customer', 'middle_name', existing_type=sa.VARCHAR(length=60), nullable=False)
    op.alter_column('customer', 'gender', existing_type=sa.VARCHAR(length=20), nullable=False)
    op.create_unique_constraint(None, 'customer', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'customer', type_='unique')
    op.alter_column('customer', 'gender', existing_type=sa.VARCHAR(length=20), nullable=False)
    op.alter_column('customer', 'middle_name', existing_type=sa.VARCHAR(length=60), nullable=False)
    op.alter_column('customer', 'last_name', existing_type=sa.VARCHAR(length=60), nullable=False)
    op.alter_column('customer', 'first_name', existing_type=sa.VARCHAR(length=60), nullable=False)
    op.alter_column('customer', 'title', existing_type=sa.VARCHAR(length=10), nullable=False)
    # ### end Alembic commands ###

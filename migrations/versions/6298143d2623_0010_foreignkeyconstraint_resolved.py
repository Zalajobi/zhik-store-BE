"""0010 ForeignKeyConstraint resolved

Revision ID: 6298143d2623
Revises: c6485e866beb
Create Date: 2022-06-04 22:27:25.247152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6298143d2623'
down_revision = 'c6485e866beb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'patients', 'provider', ['consultant_id'], ['id'], use_alter=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'patients', type_='foreignkey')
    # ### end Alembic commands ###

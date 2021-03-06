"""0011 ForeignKeyConstraint resolved

Revision ID: f812cbdc4b47
Revises: 6298143d2623
Create Date: 2022-06-05 00:20:43.239249

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f812cbdc4b47'
down_revision = '6298143d2623'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('patients', 'registration_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    op.drop_constraint('patients_registration_id_fkey', 'patients', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('patients_registration_id_fkey', 'patients', 'registration', ['registration_id'], ['id'])
    op.alter_column('patients', 'registration_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    # ### end Alembic commands ###

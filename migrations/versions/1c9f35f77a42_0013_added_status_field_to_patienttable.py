"""0013 Added status field to PatientTable

Revision ID: 1c9f35f77a42
Revises: c0e55ca7bf63
Create Date: 2022-06-05 00:28:33.348258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c9f35f77a42'
down_revision = 'c0e55ca7bf63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patients', sa.Column('status', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patients', 'status')
    # ### end Alembic commands ###
"""address table created

Revision ID: b8cbbf710beb
Revises: 8085fdc7d7c6
Create Date: 2022-05-01 04:36:26.168453

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b8cbbf710beb'
down_revision = '8085fdc7d7c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('username', sa.String(length=60), nullable=False),
    sa.Column('title', sa.String(length=10), nullable=False),
    sa.Column('first_name', sa.String(length=60), nullable=False),
    sa.Column('last_name', sa.String(length=60), nullable=False),
    sa.Column('middle_name', sa.String(length=60), nullable=False),
    sa.Column('dob', sa.Date(), nullable=True),
    sa.Column('gender', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('phone', sa.String(length=60), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('date_created', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('username'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('password'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('address',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('perm_address', sa.String(length=200), nullable=False),
    sa.Column('country', sa.String(length=60), nullable=False),
    sa.Column('state', sa.String(length=60), nullable=False),
    sa.Column('house_number', sa.String(length=60), nullable=False),
    sa.Column('flat_number', sa.String(length=60), nullable=True),
    sa.Column('zip_code', sa.String(length=10), nullable=False),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.ForeignKeyConstraint(['username'], ['customer.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('address')
    op.drop_table('customer')
    # ### end Alembic commands ###

"""0003 relationship_map_customer_socials

Revision ID: 6df6caf9fabf
Revises: 99a657bf442a
Create Date: 2022-05-04 18:10:20.692067

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6df6caf9fabf'
down_revision = '99a657bf442a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('product')
    # op.drop_table('product_images')
    op.add_column('customer', sa.Column('socials_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key(None, 'customer', 'social_accounts', ['socials_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'customer', type_='foreignkey')
    op.drop_column('customer', 'socials_id')
    op.create_table('product_images',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('product_image', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('product_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id'], ['product.id'], name='product_images_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='product_images_pkey')
    )
    op.create_table('product',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('seller_username', sa.VARCHAR(length=60), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=60), autoincrement=False, nullable=False),
    sa.Column('categories', sa.VARCHAR(length=60), autoincrement=False, nullable=False),
    sa.Column('price', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('discount', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['seller_username'], ['customer.username'], name='product_seller_username_fkey'),
    sa.PrimaryKeyConstraint('id', name='product_pkey')
    )
    # ### end Alembic commands ###

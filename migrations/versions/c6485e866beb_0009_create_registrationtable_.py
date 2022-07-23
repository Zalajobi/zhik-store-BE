"""0009 create RegistrationTable PatientTable

Revision ID: c6485e866beb
Revises: 2280fa680fa1
Create Date: 2022-06-04 22:17:39.177405

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c6485e866beb'
down_revision = '2280fa680fa1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('registration',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('specialty', sa.String(length=50), nullable=True),
    sa.Column('time_created', sa.DateTime(), nullable=False),
    sa.Column('status', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patients',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('patient_hospital_id', sa.String(length=100), nullable=True),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('middle_name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('phone_number', sa.String(length=100), nullable=False),
    sa.Column('gender', sa.String(length=100), nullable=False),
    sa.Column('title', sa.String(length=20), nullable=False),
    sa.Column('dob', sa.DateTime(), nullable=False),
    sa.Column('marital_status', sa.String(length=30), nullable=True),
    sa.Column('religion', sa.String(length=30), nullable=True),
    sa.Column('occupation', sa.String(length=100), nullable=True),
    sa.Column('patient_type', sa.String(length=10), nullable=False),
    sa.Column('registration_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('unit_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('consultant_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('next_of_kin_name', sa.String(length=100), nullable=True),
    sa.Column('next_of_kin_phone', sa.String(length=30), nullable=True),
    sa.Column('next_of_kin_address', sa.String(length=200), nullable=True),
    sa.Column('next_of_kin_relationship', sa.String(length=30), nullable=True),
    sa.Column('next_of_kin_gender', sa.String(length=100), nullable=True),
    sa.Column('next_of_kin_occupation', sa.String(length=100), nullable=True),
    sa.Column('perm_address', sa.String(length=200), nullable=True),
    sa.Column('city_name', sa.String(length=60), nullable=True),
    sa.Column('state', sa.String(length=60), nullable=True),
    sa.Column('zip_code', sa.String(length=60), nullable=True),
    sa.Column('nationality', sa.String(length=60), nullable=True),
    sa.ForeignKeyConstraint(['consultant_id'], ['providers.id'], use_alter=True),
    sa.ForeignKeyConstraint(['registration_id'], ['registration.id'], ),
    sa.ForeignKeyConstraint(['unit_id'], ['units.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_patients_patient_hospital_id'), 'patients', ['patient_hospital_id'], unique=False)
    op.add_column('provider', sa.Column('profile_image_url', sa.String(length=255), nullable=True))
    op.add_column('provider', sa.Column('patient_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key(None, 'provider', 'patients', ['patient_id'], ['id'], use_alter=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'provider', type_='foreignkey')
    op.drop_column('provider', 'patient_id')
    op.drop_column('provider', 'profile_image_url')
    op.drop_index(op.f('ix_patients_patient_hospital_id'), table_name='patients')
    op.drop_table('patients')
    op.drop_table('registration')
    # ### end Alembic commands ###

import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
# from werkzeug.security import generate_password_hash
from app.db import db as database


class PatientTable(database.Model):
    __tablename__ = 'patients'

    # BioData
    id = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    patient_hospital_id = database.Column(database.String(100), index=True)  # assigned by the hospital
    first_name = database.Column(database.String(100), nullable=False)
    last_name = database.Column(database.String(100), nullable=False)
    middle_name = database.Column(database.String(100), nullable=True)
    email = database.Column(database.String(100), nullable=False)
    phone_number = database.Column(database.String(100), nullable=False)
    gender = database.Column(database.String(100), nullable=False)
    title = database.Column(database.String(20), nullable=False)
    dob = database.Column(database.DateTime, nullable=False)
    marital_status = database.Column(database.String(30))
    religion = database.Column(database.String(30))
    occupation = database.Column(database.String(100))

    # Registration Information
    patient_type = database.Column(database.String(10), nullable=False)
    registration_id = database.Column(UUID(as_uuid=True), database.ForeignKey('registration.id'))
    unit_id = database.Column(UUID(as_uuid=True), database.ForeignKey('units.id'))
    consultant_id = database.Column(UUID(as_uuid=True), database.ForeignKey('provider.id', use_alter=True))

    # Next of Kin
    next_of_kin_name = database.Column(database.String(100))
    next_of_kin_phone = database.Column(database.String(30))
    next_of_kin_address = database.Column(database.String(200))
    next_of_kin_relationship = database.Column(database.String(30))
    next_of_kin_gender = database.Column(database.String(10))
    next_of_kin_occupation = database.Column(database.String(100))

    # Contact Information
    perm_address = database.Column(database.String(200))
    city_name = database.Column(database.String(60))
    state = database.Column(database.String(60))
    zip_code = database.Column(database.String(10))
    nationality = database.Column(database.String(60))

    consultant = database.relationship('ProviderTable', foreign_keys=[consultant_id], cascade="all,delete")
    units = database.relationship('UnitTable', foreign_keys=[unit_id], cascade="all,delete")

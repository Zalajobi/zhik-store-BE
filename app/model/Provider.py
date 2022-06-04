import uuid
from sqlalchemy.dialects.postgresql import UUID
# from werkzeug.security import generate_password_hash
from app.db import db


class ProviderTable(db.Model):
    __tablename__ = 'provider'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    phone_number = db.Column(db.String(60), nullable=False)
    username = db.Column(db.String(60), nullable=False, unique=True)
    first_name = db.Column(db.String(60), nullable=False)
    middle_name = db.Column(db.String(60), nullable=True)
    last_name = db.Column(db.String(60), nullable=False)
    dob = db.Column(db.String(60), nullable=False)
    gender = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(60), nullable=False)
    staff_id = db.Column(db.String(60), nullable=False, index=True, unique=True)
    street_address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(60), nullable=False)
    state = db.Column(db.String(60), nullable=False)
    country = db.Column(db.String(60), nullable=False)
    zipcode = db.Column(db.Integer)
    profile_image_url = db.Column(db.String(255), nullable=True)

    department_id = db.Column(UUID(as_uuid=True), db.ForeignKey('departments.id'))
    unit_id = db.Column(UUID(as_uuid=True), db.ForeignKey('units.id'))
    role_id = db.Column(UUID(as_uuid=True), db.ForeignKey('roles.id'))
    patient_id = db.Column(UUID(as_uuid=True), db.ForeignKey('patients.id', use_alter=True))
    patients = db.relationship('PatientTable', backref='provider_patients',
                               lazy=True, foreign_keys=[patient_id])

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def __repr__(self):
        return '<id {}>'.format(self.id)

from datetime import datetime

import dob as dob
from werkzeug.security import generate_password_hash
from sqlalchemy.dialects.postgresql import UUID
from db import db
import uuid


class Customer(db.Model):
    __tablename__ = 'customer'
    # id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    username = db.Column(db.String(60), nullable=False, unique=False, primary_key=True)
    title = db.Column(db.String(10), nullable=False)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    middle_name = db.Column(db.String(60), nullable=False)
    dob = db.Column(db.Date())
    gender = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    phone = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.Date(), nullable=False, default=datetime.utcnow())
    profile_image_url = db.Column(db.String(255), nullable=True)
    # address = db.relationship("address", backref='customer', lazy=True, cascade="all,delete")

    def __init__(self, first_name, last_name, middle_name, username, email, phone, password, title, gender, profile_image_url, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.username = username
        self.email = email
        self.phone = phone
        self.password = generate_password_hash(password)
        self.title = title
        self.gender = gender
        self.profile_image_url = profile_image_url
        self.dob = dob

    def __repr__(self):
        return '<username {}>'.format(self.username)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_db_data(self):
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def delete_by_username(cls, username):
        cls.query.filter_by(username=username).delete()

    @classmethod
    def get_all_customers(cls):
        return cls.query.all()

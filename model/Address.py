from db import db
import uuid
from sqlalchemy.dialects.postgresql import UUID


class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    perm_address = db.Column(db.String(200), nullable=False)
    country = db.Column(db.String(60), nullable=False)
    state = db.Column(db.String(60), nullable=False)
    house_number = db.Column(db.String(60), nullable=False)
    flat_number = db.Column(db.String(60), nullable=True)
    zip_code = db.Column(db.String(10), nullable=False)
    username = db.Column(db.String(60), db.ForeignKey("customer.username"))
    # username = db.relationship('customer', backref='customer', lazy=True, cascade="all,delete")

    def __init__(self, perm_address, country, state, house_number, flat_number, zip_code, username):
        self.perm_address = perm_address
        self.country = country
        self.state = state
        self.house_number = house_number
        self.flat_number = flat_number
        self.zip_code = zip_code
        self.username = username

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_all_by_username(cls, username):
        return cls.query.filter_by(username=username).all()

    @classmethod
    def delete_one_by_id(cls, id):
        cls.query.filter_by(id=id).delete()
        db.session.commit()

    @classmethod
    def get_one_by_username_id(cls, username, id):
        return cls.query.filter_by(username=username, id=id).first()
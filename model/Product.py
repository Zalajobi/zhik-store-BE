from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    seller_username = db.Column(db.String(60), db.ForeignKey("customer.username"))
    name = db.Column(db.String(60), nullable=False)
    categories = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, nullable=True)
    short_description = db.Column(db.String(500), nullable=True)
    description = db.Column(db.String(1500), nullable=True)
    date_added = db.Column(db.Date(), nullable=False, default=datetime.utcnow())
    weight = db.Column(db.Float, nullable=True)
    dimension = db.Column(db.String(20), nullable=True)
    product_images = db.relationship("product_images", backref='product', lazy=True, cascade="all,delete")

    # reviews, stock

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class ProductImages(db.Model):
    __tablename__ = 'product_images'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    product_image = db.Column(db.String(255))
    product_id = db.Column(UUID(as_uuid=True), db.ForeignKey("product.id"))

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
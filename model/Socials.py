from db import db
import uuid
from sqlalchemy.dialects.postgresql import UUID


class Socials(db.Model):
    __tablename__ = 'social_accounts'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    customer = db.Column(db.String(60), db.ForeignKey("customer.username"))
    linkedin = db.Column(db.String(60), nullable=True)
    facebook = db.Column(db.String(60), nullable=True)
    twitter = db.Column(db.String(60), nullable=True)
    reddit = db.Column(db.String(60), nullable=True)
    quora = db.Column(db.String(60), nullable=True)
    telegram = db.Column(db.String(60), nullable=True)
    instagram = db.Column(db.String(60), nullable=True)
    wechat = db.Column(db.String(60), nullable=True)
    sina = db.Column(db.String(60), nullable=True)
    tiktok = db.Column(db.String(60), nullable=True)
    snapshot = db.Column(db.String(60), nullable=True)
    pin_interest = db.Column(db.String(60), nullable=True)
    discord = db.Column(db.String(60), nullable=True)
    signal = db.Column(db.String(60), nullable=True)
    skype = db.Column(db.String(60), nullable=True)
    line = db.Column(db.String(60), nullable=True)
    slack = db.Column(db.String(60), nullable=True)
    medium = db.Column(db.String(60), nullable=True)

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

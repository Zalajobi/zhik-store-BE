from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declared_attr

from app.db import db as database


class RoleTable(database.Model):
    """
    One-to-Many relationship with provider table
    """

    __tablename__ = 'roles'

    id = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    name = database.Column(database.String(60), nullable=False)
    time_created = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    time_updated = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    description = database.Column(database.Text)

    provider_roles = database.relationship('ProviderTable', backref='role', lazy=True)

    def save_to_db(self):
        database.session.add(self)
        database.session.commit()

    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @declared_attr
    def __repr__(self):
        return '<Role: {}>'.format(self.name)
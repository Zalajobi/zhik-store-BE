from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db as database


class UnitTable(database.Model):

    ACTIVE_STATUS = 'active'
    INACTIVE_STATUS = 'inactive'

    __tablename__ = 'units'

    id = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    name = database.Column(database.String(100))
    specialty = database.Column(database.String(50))
    time_created = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    status = database.Column(database.String(100), default=ACTIVE_STATUS)

    providers = database.relationship('ProviderTable', backref='provider_unit', lazy=True)

    def save_to_db(self):
        database.session.add(self)
        database.session.commit()

    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def __repr__(self):
        return '<Unit name: {}>'.format(self.name)
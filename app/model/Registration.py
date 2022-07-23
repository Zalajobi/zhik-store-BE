import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from app.db import db as database


class RegistrationTable(database.Model):
    ACTIVE_STATUS = 'active'
    INACTIVE_STATUS = 'inactive'

    __tablename__ = 'registration'

    id = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)

    name = database.Column(database.String(100))
    specialty = database.Column(database.String(50))
    time_created = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    status = database.Column(database.String(100), default=ACTIVE_STATUS)

    # providers = database.relationship('ProviderTable', backref='provider_unit', lazy=True)
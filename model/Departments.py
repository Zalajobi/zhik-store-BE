from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db


class DepartmentTable(db.Model):
    __tablename__ = 'departments'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    name = db.Column(db.String(100))
    time_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)

    providers = db.relationship('ProviderTable', backref='department', lazy=True)

    def __repr__(self):
        return '<Department: {}>'.format(self.name)

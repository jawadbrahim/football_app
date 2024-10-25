from dataclasses import dataclass
import uuid
import datetime
from sqlalchemy.dialects.postgresql import UUID
from database.postgres import db
@dataclass
class User(db.Model):
    id=db.Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key=True)
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))
    is_deleted=db.Column(db.Boolean,default=False)
    created_at=db.Column(db.DateTime(default=datetime.datetime.now(datetime.timezone.utc)))
    
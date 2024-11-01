from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database.postgres import db
import datetime

@dataclass
class Match(db.Model):
    id=db.Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key=True)
    duration=db.Column(db.Integer,nullable=False)
    location=db.Column(db.String(1000),nullable=False)
    is_public=db.Column(db.Boolean,default=True)
    created_at=db.Column(db.DateTime,default=datetime.datetime.now(datetime.timezone.utc))
    user_id=db.Column("user_id",UUID(as_uuid=True),db.ForeignKey("user.id"))
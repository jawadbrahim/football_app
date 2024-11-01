from database.postgres import db
from dataclasses import dataclass
import uuid
import datetime
from sqlalchemy.dialects.postgresql import UUID

@dataclass
class Profile(db.Model):
    id=db.Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key=True)
    age=db.Column(db.Integer,nullable=False)
    skill_level=db.Column(db.String(100),nullable=False)
    position=db.Column(db.String(20),nullable=False)
    bio=db.Column(db.Text,nullable=True)
    created_at=db.Column(db.DateTime,default=datetime.datetime.now(datetime.timezone.utc))
    user_id=db.Column("user_id",UUID(as_uuid=True),db.ForeignKey("user.id"),nullable=False,unique=False)


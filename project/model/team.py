from database.postgres import db
from dataclasses import dataclass
import uuid
import datetime
from sqlalchemy.dialects.postgresql import UUID

@dataclass
class Team(db.Model):
    id=db.Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key=True)
    number_of_player=db.Column(db.Integer,nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.datetime.utcnow())
    user_id=db.Column("user_id",UUID(as_uuid=True),db.ForeignKey("user.id"),nullable=False)
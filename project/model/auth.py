from database.postgres import db
from dataclasses import dataclass
import uuid
from sqlalchemy.dialects.postgresql import UUID
import datetime

@dataclass
class Auth(db.Model):
  id = db.Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key=True)
  email=db.Column(db.String(100))
  password=db.Column(db.String(100))
  created_at=db.Column(db.DateTime,default=datetime.datetime.now(datetime.timezone.utc))
  is_deleted=db.Column(db.Boolean,default=False)
  token_id=db.Column("token_id",UUID(as_uuid=True),db.ForeignKey("token.id"))
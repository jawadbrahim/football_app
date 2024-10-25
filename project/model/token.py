from database.postgres import db
import uuid
import datetime
from sqlalchemy.dialects.postgresql import UUID
from dataclasses import dataclass

@dataclass
class Token(db.Model):
    id=db.Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key=True)
    token=db.Column(db.String)
    created_At=db.Column(db.DateTime,default=datetime.datetime.now(datetime.timezone.utc))
    

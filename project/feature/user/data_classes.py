from dataclasses import dataclass
from datetime import datetime
import uuid

@dataclass
class UserDataClass:
    id:uuid.UUID
    first_name:str
    last_name:str
    created_at:datetime
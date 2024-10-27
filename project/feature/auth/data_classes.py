from dataclasses import dataclass
import uuid
from datetime import datetime
@dataclass
class AuthDataClass:
    id:uuid.UUID
    email:str
    password:str
    created_at:datetime
@dataclass
class Login:
    id:uuid.UUID
    email:str
    password:str
    token:str

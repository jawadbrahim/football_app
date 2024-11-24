from dataclasses import dataclass
import uuid
from datetime import datetime
from typing import Optional
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
@dataclass
class GoogleDataClass:
    id:uuid.UUID
    token:str
    
from dataclasses import dataclass
from datetime import datetime
import uuid

@dataclass
class UserDataClass:
    id:uuid.UUID
    first_name:str
    last_name:str
    created_at:datetime
@dataclass
class UsersDataClass:
    id:uuid.UUID
    first_name:str
    last_name:str
@dataclass
class ProfileDataClass:
    id:uuid.UUID
    age:int
    skill_level:str
    position:str
    bio:str
    created_at:datetime
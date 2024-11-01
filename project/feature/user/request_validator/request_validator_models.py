from pydantic import BaseModel
from typing import Optional


class UserModel(BaseModel):
    first_name:str
    last_name:str

class ProfileModel(BaseModel):
    age:int
    skill_level:str
    position:str
    bio: Optional[str]=None


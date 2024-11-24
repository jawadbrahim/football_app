from pydantic import BaseModel
from typing import Optional,Literal


class UserModel(BaseModel):
    first_name:str
    last_name:str

class ProfileModel(BaseModel):
    age:int
    skill_level:Literal["beginner","intermediate","expert"]
    position:Literal["CB", "RB", "LB", "GK", "CM", "CAM", "CDM", "RW", "LW", "CF"]
    bio: Optional[str]=None


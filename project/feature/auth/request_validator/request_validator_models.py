
from pydantic import BaseModel

class RegisterModel(BaseModel):
    email:str
    password:str

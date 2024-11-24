
from pydantic import BaseModel

class RegisterModel(BaseModel):
    email:str
    password:str
class GoogleModel(BaseModel):
    token:str
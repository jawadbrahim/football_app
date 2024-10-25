
from pydantic import BaseModel

class RegisterModel(BaseModel):
    email:str
    passwrod:str

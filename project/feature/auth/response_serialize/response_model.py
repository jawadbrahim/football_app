from ..data_classes import AuthDataClass,Login,GoogleDataClass
from pydantic import BaseModel
from typing import Optional
class AuthModel(BaseModel):
    auth:AuthDataClass
class LoginModel(BaseModel):
    account:Login
class GoogleModel(BaseModel):
    google:GoogleDataClass
class GoogleStatus(BaseModel):
    status:str
    google:Optional[GoogleDataClass]=None
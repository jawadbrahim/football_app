from ..data_classes import AuthDataClass,Login
from pydantic import BaseModel
class AuthModel(BaseModel):
    auth:AuthDataClass
class LoginModel(BaseModel):
    account:Login
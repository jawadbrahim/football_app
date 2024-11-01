from pydantic import BaseModel
from ..data_classes import UserDataClass,UsersDataClass,ProfileDataClass

class UserSerializeModel(BaseModel):
    user:UserDataClass
class UsersSerializeModel(BaseModel):
  users:UsersDataClass
class UserProfileModel(BaseModel):
   user_profile:ProfileDataClass
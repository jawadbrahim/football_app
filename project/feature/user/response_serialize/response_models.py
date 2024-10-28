from pydantic import BaseModel
from ..data_classes import UserDataClass

class UserSerializeModel(BaseModel):
    user:UserDataClass
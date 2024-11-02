from ..data_classes import MatchDataClass,UpdateMatch
from pydantic import BaseModel

class MatchSerializeModel(BaseModel):
    match:MatchDataClass
class updateModel(BaseModel):
    update_match:UpdateMatch
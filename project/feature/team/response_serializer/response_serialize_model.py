from pydantic import BaseModel
from ..data_classe import MatchDataClass


class TeamSerializeModel(BaseModel):
    team:MatchDataClass
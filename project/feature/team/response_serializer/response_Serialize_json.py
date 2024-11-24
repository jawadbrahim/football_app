from .abstraction import AbstractionResponseSerializer
from .response_serialize_model import TeamSerializeModel


class TeamSerialize(AbstractionResponseSerializer):
    def serialize_create_team(self,team):
        reponse=TeamSerializeModel(team=team)
        return reponse.json()
        
        
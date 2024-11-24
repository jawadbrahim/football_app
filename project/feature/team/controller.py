from .data_access.factory import FactoryDataAccess
from .response_serializer.factory import FactoryResponseSerialize
from.team_service.factory import FactoryTeamSertvice
from .exception import TeamNotFound
from flask import jsonify

class TeamController:
    def __init__(self):
        self.data_access=FactoryDataAccess.build_object()
        self.team_service=FactoryTeamSertvice.build_object(self.data_access)
        self.response_Serialize=FactoryResponseSerialize.build_object()


    def create_team(self,validate_data):
        try:
         team=self.team_service.create_team(validate_data.user_id,validate_data.number_of_player)
         self.data_access.commit()
         return self.response_Serialize.serialize_create_team(team)
        except(TeamNotFound,Exception)as e:
           return jsonify({"error":e.to_dict()})

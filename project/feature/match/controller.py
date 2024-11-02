from .data_access.factory import FactoryDataAccess
from .match_service.factory import FactoryAuthService
from .response_serialize.factory import FactoryResponseSeriaizer
from .excption import MatchNotFound
from flask import jsonify

class MatchController:

    def __init__(self):
        self.data_access=FactoryDataAccess.build_object()
        self.auth_service=FactoryAuthService.build_object(self.data_access)
        self.response_Serializer=FactoryResponseSeriaizer.build_object()

    def create_match(self,validate_data):
        try:
         match=self.auth_service.create_match(validate_data.duration,validate_data.location)
         self.data_access.commit()
         return self.response_Serializer.serialize_match(match)
        except(MatchNotFound,Exception)as e:
           return jsonify({"error":e.to_dict()})
        
    
    
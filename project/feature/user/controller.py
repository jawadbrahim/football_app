from .data_access.factory import FactoryDataAccess
from .user_service.factory import FactoryUserService
from .response_serialize.factory import FactoryResponseJson
from .exception import UserNotFound
from flask import jsonify
class UserController:

    def __init__(self):
        self.data_access=FactoryDataAccess.build_object()
        self.user_service=FactoryUserService.build_object(self.data_access)
        self.response_serialize=FactoryResponseJson.build_object()


    def create_user(self,validate_data):
        try:
         user=self.user_service.create_user(validate_data.first_name,validate_data.last_name)
         self.data_access.commit()
         return self.response_serialize.serialize_create_user(user)
        except(UserNotFound,Exception)as e:
           return jsonify({"error":e.to_dict()})
    def get_user(self,user_id):
       try:
          get_user=self.user_service.get_user(user_id)
          return get_user
       except(UserNotFound ,Exception)as e:
          return jsonify({"error":e.to_dict()})
    def delete_user(self,user_id):
       try:
          deleted_user=self.user_service.delete_user(user_id)
          self.data_access.commit()
          return deleted_user
       except(UserNotFound,Exception)as e:
          return jsonify({"error":e.to_dict()})
    
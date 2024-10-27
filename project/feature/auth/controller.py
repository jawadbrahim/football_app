from .data_access.factory import FactoryDataAccess
from .auth_service.factory import FactoryDefault
from .response_serialize.factory import FactoryResponse
from .exception import EmailAlreadyExist,CredentialMismatch,UserNotFound
from flask import jsonify
class AuthController:
    def __init__(self):
        self.data_access=FactoryDataAccess.build_object()
        self.auth_service=FactoryDefault.build_object(self.data_access)
        self.response_serialize=FactoryResponse.build_object()


    def register(self,validate_data):
        try:
         auth=self.auth_service.register(validate_data.email,validate_data.password)
         self.data_access.commit()
         return self.response_serialize.serialize_auth(auth)
        except(UserNotFound,Exception)as e:
           return jsonify({"error":e.to_dict()}) 
    def login(self,validate_data):
       try:
          account=self.auth_service.login(validate_data.email,validate_data.password)
          self.data_access.commit()
          return self.response_serialize.serialize_login(account)
       except (CredentialMismatch , Exception) as e :
          return jsonify({"error":e.to_dict()})
          
    
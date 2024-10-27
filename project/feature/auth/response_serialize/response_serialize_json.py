from .abstraction import AbstractionResponseSerialize
from .response_model import AuthModel,LoginModel

class ResponseJon(AbstractionResponseSerialize):

    def serialize_auth(self,auth):
        response=AuthModel(auth=auth)
        return response.json()
    def serialize_login(self,account):
        response=LoginModel(account=account)
        return response.json()

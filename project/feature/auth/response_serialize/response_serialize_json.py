from .abstraction import AbstractionResponseSerialize
from .response_model import AuthModel,LoginModel,GoogleModel,GoogleStatus

class ResponseJon(AbstractionResponseSerialize):

    def serialize_auth(self,auth):
        response=AuthModel(auth=auth)
        return response.json()
    def serialize_login(self,account):
        response=LoginModel(account=account)
        return response.json()
    def serialize_google(self,google):
        response=GoogleModel(google=google)
        return response.json()
    def serialize_google_status(self,status,google):
        response=GoogleStatus(status=status,google=google)
        return response.json()
     

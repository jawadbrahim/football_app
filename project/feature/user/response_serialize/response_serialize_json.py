from .abstraction import AbstractionResponseSerialize
from .response_models import UserSerializeModel,UsersSerializeModel,UserProfileModel

class SerializeJson(AbstractionResponseSerialize):
    def serialize_create_user(self,user):
        response=UserSerializeModel(user=user)
        return response.json()
    def serialize_User(self,users):
        response=UsersSerializeModel(users=users)
        return response.json()
    def serialize_create_profile(self,user_profile):
        response=UserProfileModel(user_profile=user_profile)
        return response.json()
    def serialize_get_profile(self,profile):
        response=UserProfileModel(profile=profile)
        return response.json()
        
        

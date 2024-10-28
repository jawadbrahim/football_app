from .abstraction import AbstractionResponseSerialize
from .response_models import UserSerializeModel

class SerializeJson(AbstractionResponseSerialize):
    def serialize_create_user(self,user):
        response=UserSerializeModel(user=user)
        return response.json()

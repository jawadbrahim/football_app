from .abstraction import AbstractionResponseSerialze
from .response_serialize_model import updateModel,MatchSerializeModel


class Response_Json(AbstractionResponseSerialze):
    def serialize_match(self,match):
        response=MatchSerializeModel(match=match)
        return response.json()
    def serialize_update_match(self,update_match):
        response=updateModel(update_match=update_match)
        return response.json()
        
from .abstraction import AbstractionReqeustValidator
from .request_validator_model import MatchCreateModel,MatchUpdateModel
from project.decorator.validate import validate_schema

class RequestValidator(AbstractionReqeustValidator):
    def validate_create_match(self):
        return validate_schema(json_schema=MatchCreateModel)
    def validate_update_match(self):
        return validate_schema(json_schema=MatchUpdateModel)
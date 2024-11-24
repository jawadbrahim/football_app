from project.decorator.validate import validate_schema
from .abstraction import AbstractionReqeustValidator
from .request_validator_model import MatchModel

class MatchValidator(AbstractionReqeustValidator):
    def validate_create_match(self):
        return validate_schema(json_schema=MatchModel)
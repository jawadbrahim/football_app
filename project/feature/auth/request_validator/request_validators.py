from .abstraction import AbstreactionReqeustvalidator
from .request_validator_models import RegisterModel
from project.decorator.validate import validate_schema

class RequestValidatorRegister(AbstreactionReqeustvalidator):
    def validate_register(self):
        return validate_schema(json_schema=RegisterModel)
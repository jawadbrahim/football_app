from ..setting.option import RequestValidatorOption
from ..setting.development import Development
from .request_validators import ValidateUser

class FactoryRequestValidator:
    @staticmethod
    def build_object(service=Development.REQUEST_VALIDATOR):
        if service == RequestValidatorOption.PYDANTIC_MODEL:
            return ValidateUser()
        raise NotImplementedError()
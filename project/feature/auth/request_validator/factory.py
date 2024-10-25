from ..setting.development import Development
from ..setting.option import RequestValidatorOption
from .request_validators import RequestValidatorRegister


class FActoryRequestValidator:
    @staticmethod
    def build_object(service=Development.REQUEST_VALIDATOR):
        if service ==RequestValidatorOption.PYDANTIC_MODEL:
            return RequestValidatorRegister()
        raise NotImplementedError()
from ..setting.development import Development
from ..setting.option import ResponseSerializeOption
from .response_serialize_json import ResponseJon


class FactoryResponse:
    @staticmethod
    def build_object(service=Development.RESPONSE_SERIALIZE):
        if service==ResponseSerializeOption.PYDANTIC_JSON:
            return ResponseJon()
        raise NotImplementedError()
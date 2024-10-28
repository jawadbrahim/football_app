from ..setting.development import Development
from ..setting.option import ResponseSerializeOption
from .response_serialize_json import SerializeJson


class FactoryResponseJson:
    @staticmethod
    def build_object(service=Development.RESPONSE_SERIALIZE):
        if  service == ResponseSerializeOption.PYDANTIC_JSON:
            return SerializeJson()
        raise NotImplementedError()
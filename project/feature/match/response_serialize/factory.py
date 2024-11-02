from ..setting.development import Development
from ..setting.option import ResponseSerializeOption
from .resppnse_serialize_json import Response_Json


class FactoryResponseSeriaizer:
    @staticmethod
    def build_object(service=Development.RESPONSE_SERIALIZE):
        if service == ResponseSerializeOption.PYDANTIC_JSON:
            return Response_Json()
        raise NotImplementedError()
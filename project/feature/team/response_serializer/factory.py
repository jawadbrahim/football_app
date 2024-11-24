from ..setting.development import Development
from ..setting.option import ResponseSerializeOption
from .response_Serialize_json import TeamSerialize



class FactoryResponseSerialize:
    @staticmethod
    def build_object(service=Development.RESPONSE_SERIALIZE):
        if service == ResponseSerializeOption.PYDANTIC_JSON:
            return TeamSerialize()
        raise NotImplementedError()
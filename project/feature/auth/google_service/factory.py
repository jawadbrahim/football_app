from ..setting.development import Development
from ..setting.option import GoogleServiceOption
from .service import Google


class FactoryGoogle:
    @staticmethod
    def build_object(data_access,service=Development.GOOGLE_SERVICE):
        if service == GoogleServiceOption.GOOGLE:
            return Google(data_access)
        raise NotImplementedError()
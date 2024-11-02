from ..setting.development import Development
from ..setting.option import AuthServiceOption
from .default import Default


class FactoryAuthService:
    @staticmethod
    def build_object(data_access,service=Development.AUTH_SERVICE):
        if service == AuthServiceOption.DEFAULT:
            return Default(data_access)
        raise NotImplementedError()
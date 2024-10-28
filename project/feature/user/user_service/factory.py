from ..setting.development import Development
from ..setting.option import UserServiceOption
from .default import Default


class FactoryUserService:
    @staticmethod
    def build_object(data_access,service=Development.USER_SERVICE):
        if service==UserServiceOption.DEFAULT:
            return Default(data_access)
        raise NotImplementedError()
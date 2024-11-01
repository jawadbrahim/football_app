import abc

class AbstractionDataAccess(metaclass=abc.ABCMeta):
    def create_user(self):
        raise NotImplementedError()
    def create_profile(self):
        raise NotImplementedError()
    def get_profile(self):
        raise NotImplementedError()
    def get_user(self):
        raise NotImplementedError
    def delete_user(self):
        raise NotImplementedError()
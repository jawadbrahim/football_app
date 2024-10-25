import abc
class AbsteractionDataAccess(metaclass=abc.ABCMeta):
    def create_auth(self):
        raise NotImplementedError()
    def get_auth(self):
        raise NotImplementedError()
    def delete_auth(self):
        raise NotImplementedError()
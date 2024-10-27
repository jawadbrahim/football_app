import abc

class AbstractionUserService(metaclass=abc.ABCMeta):
    def create_user(self):
        raise NotImplementedError()
    def get_user(self):
     raise NotImplementedError()
    def delete_user(self):
       raise NotImplementedError()
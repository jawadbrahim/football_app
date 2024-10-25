import abc

class AbstractionAuthService(metaclass=abc.ABCMeta):
    def register(self):
        raise NotImplementedError()
    def login(self):
        raise NotImplementedError()
    
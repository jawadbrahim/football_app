import abc

class AbstractionGoogleService(metaclass=abc.ABCMeta):
    def get_status(self):
        raise NotImplementedError()
    def register(self):
        raise NotImplementedError()
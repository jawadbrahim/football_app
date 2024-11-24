import abc 

class AbstractionResponseSerialize(metaclass=abc.ABCMeta):
    def serialize_auth(self):
        raise NotImplementedError()
    def serialize_google(self):
        raise NotImplementedError()

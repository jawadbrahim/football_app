import abc

class AbstractionResponseSerialze(metaclass=abc.ABCMeta):
    def serialize_match(self):
        raise NotImplementedError()
    def serialize_update_match(self):
        raise NotImplementedError()
    
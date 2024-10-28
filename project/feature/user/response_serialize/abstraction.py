import abc

class AbstractionResponseSerialize(metaclass=abc.ABCMeta):
    def serialize_create_user(self):
        raise NotImplementedError()
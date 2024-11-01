import abc

class AbstractionResponseSerialize(metaclass=abc.ABCMeta):
    def serialize_create_user(self):
        raise NotImplementedError()
    def serialize_User(self):
        raise NotImplementedError()
    def serialize_create_profile(self):
        raise NotImplementedError()
    def serialize_get_profile(self):
        raise NotImplementedError()
import abc

class AbstractionResponseSerializer(metaclass=abc.ABCMeta):
    def serialize_create_team(self):
        raise NotImplementedError()
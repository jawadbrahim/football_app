import  abc

class AbstractionReqeustValidator(metaclass=abc.ABCMeta):
    def validate_create_match(self):
        raise NotImplementedError()
import abc 
class AbstreactionReqeustvalidator(metaclass=abc.ABCMeta):
    def validate_register(self):
        raise NotImplementedError()
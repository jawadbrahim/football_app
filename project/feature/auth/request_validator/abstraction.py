import abc 
class AbstreactionReqeustvalidator(metaclass=abc.ABCMeta):
    def validate_register(self):
        raise NotImplementedError()
    def validate_google(self):
        raise NotImplementedError()
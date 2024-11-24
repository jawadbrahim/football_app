import abc 

class AbstractionService(metaclass=abc.ABCMeta):
    def create_team(self):
        raise NotImplementedError()
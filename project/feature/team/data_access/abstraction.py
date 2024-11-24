import abc 

class AbstractionDataAccess(metaclass=abc.ABCMeta):
    def create_team(self):
        raise NotImplementedError()
    def get_team(self):
        raise NotImplementedError()
    
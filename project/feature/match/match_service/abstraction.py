import abc

class AbstractionService(metaclass=abc.ABCMeta):
    def create_match(self):
        raise NotImplementedError()
    def get_match(self):
        raise NotImplementedError()
    def update_match(self):
        raise NotImplementedError()
    def delete_match(self):
        raise NotImplementedError()
    def search_match(self):
        raise NotImplementedError()
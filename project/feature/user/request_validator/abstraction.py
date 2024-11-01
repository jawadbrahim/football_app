import abc

class AsbtractionRequestValidator(metaclass=abc.ABCMeta):
    def validate_create_user(self):
        raise NotImplementedError()
    def valdiate_create_profile(self):
        raise NotImplementedError()
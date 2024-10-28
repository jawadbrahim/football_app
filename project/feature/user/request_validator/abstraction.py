import abc

class AsbtractionRequestValidator(metaclass=abc.ABCMeta):
    def validate_create_user(self):
        raise NotImplementedError()
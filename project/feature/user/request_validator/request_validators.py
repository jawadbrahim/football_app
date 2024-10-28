from .abstraction import AsbtractionRequestValidator
from .request_validator_models import UserModel
from project.decorator.validate import validate_schema
class ValidateUser(AsbtractionRequestValidator):
    def validate_create_user(self):
        return validate_schema(json_schema=UserModel)
from .abstraction import AbstractionAuthService
from ..exception import UserNotFound,EmailAlreadyExist,CredentialMismatch
class Default(AbstractionAuthService):

    def __init__(self,data_access):
        self.data_access=data_access

    def register(self,email,password):
        exist=self.data_access.email_exist(email)
        if exist:
            return EmailAlreadyExist(email=email)
        account=self.data_access.create_auth(email,password)
        if not account:
            raise UserNotFound
        return account
    def login(self,email,passowrd):
        exist=self.data_access.email_exist(email)
        if not exist or not passowrd:
            raise CredentialMismatch(email=email)


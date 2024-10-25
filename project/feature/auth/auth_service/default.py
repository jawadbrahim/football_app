from .abstraction import AbstractionAuthService
from ..exception import UserNotFound,EmailAlreadyExist,CredentialMismatch
from project.helper.hashing import HashingHelper
class Default(AbstractionAuthService):

    def __init__(self,data_access):
        self.data_access=data_access
        self.hash_password=HashingHelper()

    def register(self,email,password):
        exist=self.data_access.email_exist(email)
        if exist:
            return EmailAlreadyExist(email=email)
        hashed_password=self.hash_password.hash_password(password)
        account=self.data_access.create_auth(email,hashed_password)
        if not account:
            raise UserNotFound
        return account
    def login(self,email,passowrd):
        exist=self.data_access.email_exist(email)
        if not exist or not self.hash_password.verify_password(passowrd,exist.password):
            raise CredentialMismatch(email=email)


from .abstraction import AbstractionAuthService
from ..exception import UserNotFound

class Default(AbstractionAuthService):

    def __init__(self,data_access):
        self.data_access=data_access

    def register(self,email,password):
        account=self.data_access.create_auth(email,password)
        if not account:
            raise UserNotFound
        return account
    def login(self):
        

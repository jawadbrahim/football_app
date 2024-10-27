from .abstraction import AbstractionAuthService
from ..exception import UserNotFound,EmailAlreadyExist,CredentialMismatch
from project.helper.hashing import HashingHelper
from ..data_classes import AuthDataClass,Login
from project.helper.jwt import JwtHelper
from project.helper.date import DateHeler
from project.feature.auth.config.development import Config
from project.feature.auth.config.development import Development
import uuid
class Default(AbstractionAuthService):

    def __init__(self,data_access):
        self.data_access=data_access
        self.hash_password=HashingHelper()
        self.jwt_helper=JwtHelper(Development.JWT_SECRET,Development.JWT_ALGORITHM)
        self.date_helper=DateHeler()

    def generate_token(self):
        token_id=uuid.uuid4()
        exp=self.date_helper.expired_time(Config.JWT_DURATION_IN_MINUTE)
        payload={
            "token_id":str(token_id),
            "exp":exp
        }
        token_str=self.jwt_helper.encode(payload)
        self.data_access.insert_token(token_id,token_str)
        return token_id,token_str

        

    def register(self,email,password):
        exist=self.data_access.email_exist(email)
        if exist:
            raise EmailAlreadyExist(email=email)
        hashed_password=self.hash_password.hash_password(password)
        auth=self.data_access.create_auth(email,hashed_password)
        if not auth:
            raise UserNotFound
        return AuthDataClass(
            id=auth.id,
            email=auth.email,
            password=auth.password,
            created_at=auth.created_at


        )
    def login(self,email,password):
        account=self.data_access.email_exist(email)
        if not account or not self.hash_password.verify_password(password,account.password):
            raise CredentialMismatch(email=email)
        token_id,token_str=self.generate_token()
        self.data_access.update_token_auth_id(account.id,token_id)
        return Login(
            id=account.id,
            email=account.email,
            password=account.password,
            token=token_str
        )



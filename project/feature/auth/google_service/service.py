from .abstraction import AbstractionGoogleService
from ..exception import GoogleAlreadyExist,InvalidToken
from project.helper.date import DateHeler
from project.helper.google import GoogleAuth
from ..config.development import Config
from project.helper.jwt import JwtHelper
from project.helper.hashing import HashingHelper
from project.config.development import Development
from ..data_classes import GoogleDataClass
import uuid
class Google(AbstractionGoogleService):
    def __init__(self, data_access):
        self.data_access = data_access
        self.date_helper = DateHeler()
        self.hashing_helper = HashingHelper()
        self.jwt_helper = JwtHelper(Config.JWT_ALGORITHM, Config.JWT_SECRET)
        self.google_helper = GoogleAuth(Development.GOOGLE_AUTH_CLIENT_ID)

    def generate_token(self):
        token_id = uuid.uuid4()
        exp = self.date_helper.expired_time(Config.JWT_DURATION_IN_MINUTE)
        payload = {
            "token_id": str(token_id),
            "exp": exp
        }
        token_str = self.jwt_helper.encode(payload)
        self.data_access.insert_token(token_id, token_str)
        return token_id,token_str

    def get_status(self, token):
        google_payload = self.google_helper.verifiy_id(token)
        if not google_payload:
            raise InvalidToken(token=token)

        google_auth = self.data_access.get_google_auth(google_payload["sub"])
        if not google_auth:
            return "unauthenticated", None

        access_token = self.generate_token()
        self.data_access.update_token_auth_id(google_auth.id, access_token)

        google_auth = GoogleDataClass(
            id=google_auth.id,
            email=google_auth.email,
            token=google_auth.token,
            user_id=google_auth.user_id
        )
        return "authenticated", google_auth

    def register(self, token):
     google_payload = self.google_helper.verifiy_id(token)
     if not google_payload:
        raise InvalidToken(token=token)

     google_auth = self.data_access.get_google_auth(google_payload["sub"])
     if google_auth:
        raise GoogleAlreadyExist(google_id=google_payload["sub"])
     self.data_access.insert_google(google_payload)
     google_auth = self.data_access.get_google_auth(google_payload["sub"])
 
     if not google_auth:
        raise Exception("Failed to create Google auth record.")
     token_id, token_str = self.generate_token()
     self.data_access.update_token_auth_id(google_auth.id, token_id)

     return GoogleDataClass(
        id=google_auth.id,
        token=token_str,
    )


        
        


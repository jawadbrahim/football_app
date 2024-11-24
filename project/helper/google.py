from google.oauth2 import id_token
from google.auth.transport import requests
class GoogleAuth:
    def __init__(self,client_id):
        self.client_id=client_id
    def verifiy_id(Self,token):
     try:
        id_info=id_token.verify_token(token,requests.Request(),Self.client_id)
        return id_info
     except ValueError as e:
        print("invalid token",str(e))
        return None
        
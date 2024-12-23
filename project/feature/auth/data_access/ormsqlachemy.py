from .abstraction import AbsteractionDataAccess
from project.module.ormsqlachemy import Orm 
from project.model.auth import Auth
from project.model.token import Token
from project.model.auth_google import Google

class OrmSqlAlchemy(AbsteractionDataAccess,Orm):
    
    def create_auth(self,email,password):
        account=Auth(email=email,
                  password=password)
        
        self.add_and_flush(account)
        return account
    def get_auth(self,auth_id):
        auth=Auth.query.filter(Auth.id==auth_id,Auth.is_deleted==False).first()
        return auth
    def email_exist(self,email):
        exist=Auth.query.filter(Auth.email==email,Auth.is_deleted==False).first()
        return exist
    def email_password_match(self,email,password):
        account_matched=Auth.query.filter(Auth,email==email,Auth.password==password,Auth.is_deleted==False).first()
        return  account_matched
    def insert_auth(self):
        auth=Auth(

        )
        self.add_and_flush(auth)
        return auth.id
    
    def delete_auth(self,auth_id):
        deleted_auth=Auth.query.filter(Auth.id==auth_id).first()
        if deleted_auth:
            deleted_auth.is_deleted = True
        return deleted_auth
    def get_google_auth(self, google_account_id):
        google = Google.query.filter(
            Google.google_account_id == google_account_id,
            Google.is_deleted == False
        ).first()
        return google

    def insert_google(self, google_payload):
        google_auth = Google(
            google_account_id=google_payload["sub"], 
            payload=google_payload
        )
        self.add_and_flush(google_auth)
        return google_auth.id

    
    def insert_token(self,token_id,token_str):
        token=Token(
           id=token_id,
           token=token_str

        )
        self.add(token)
        return token
    def update_token_auth_id(self,auth_id,token_id):
        auth_record=Auth.query.filter(Auth.id==auth_id).first()
        if auth_record:
            auth_record.token_id=token_id
        return auth_record
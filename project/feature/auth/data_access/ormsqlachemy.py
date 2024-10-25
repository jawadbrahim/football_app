from .abstraction import AbsteractionDataAccess
from project.module.ormsqlachemy import Orm 
from project.model.auth import Auth



class OrmSqlAlchemy(AbsteractionDataAccess,Orm):
    
    def create_auth(self,email,password):
        account=Auth(email=email,
                  password=password)
        self.add(account)
        return account
    def get_auth(self,auth_id):
        auth=Auth.query.filter(Auth.id==auth_id,Auth.is_deleted==False).first()
        return auth
    
    def delete_auth(self,auth_id):
        deleted_auth=Auth.query.filter(Auth.id==auth_id).first()
        if deleted_auth:
            deleted_auth.is_deleted = True
        return deleted_auth
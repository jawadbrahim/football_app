from database.postgres import db
from .abstraction import AbstractionDataAccess
from project.model.user import User
from project.module.ormsqlachemy import Orm


class OrmSqlAlchemy(AbstractionDataAccess,Orm):
    
    def create_user(self,first_name,last_name):
        user=User(
            first_name=first_name,
            last_name=last_name
        )
        self.add(user)
        return user
    def get_user(self,user_id):
        get_user=User.query.filter(User.id==user_id,User.is_deleted==False).first()
        return get_user
    def delete_user(self,user_id):
        deleted_user=User.query.filter(User.id==user_id).first()
        if deleted_user:
            deleted_user.is_deleted=True
        return deleted_user
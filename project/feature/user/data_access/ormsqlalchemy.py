from database.postgres import db
from .abstraction import AbstractionDataAccess
from project.model.user import User
from project.model.user_profile import Profile
from project.module.ormsqlachemy import Orm


class OrmSqlAlchemy(AbstractionDataAccess,Orm):
    
    def create_user(self,first_name,last_name):
        user=User(
            first_name=first_name,
            last_name=last_name
        )
        self.add_and_flush(user)
        return user
    def create_profile(self,user_id,age,skill_level,position,bio):
        user_profile=Profile(user_id=user_id,age=age,skill_level=skill_level,position=position,bio=bio)
        self.add_and_flush(user_profile)
        return user_profile
    def get_profile(self,profile_id):
        profile=Profile.query.filter(Profile.id==profile_id).first()
        return profile

    def get_user(self,user_id):
        get_user=User.query.filter(User.id==user_id,User.is_deleted==False).first()
        return get_user
    def delete_user(self,user_id):
        deleted_user=User.query.filter(User.id==user_id).first()
        if deleted_user:
            deleted_user.is_deleted=True
        return deleted_user
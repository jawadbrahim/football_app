from .abstraction import AbstractionUserService
from ..exception import UserNotFound
from ..data_classes import UserDataClass
class Default(AbstractionUserService):

    def __init__(self,data_Access):
        self.data_access=data_Access

    def create_user(self,first_name,last_name):
        user=self.data_access.create_user(first_name,last_name)
        if not user:
            raise UserNotFound
        return UserDataClass(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            created_at=user.created_at
        )
    def get_user(self,user_id):
        get_user=self.data_access.get_user(user_id)
        if not get_user:
            return UserNotFound(user_id=user_id)
        return get_user
    def delete_user(self,user_id):
        deleted_user=self.data_access.delete_user(user_id)
        if not deleted_user:
            raise UserNotFound(user_id=user_id)
        return deleted_user



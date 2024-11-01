from .abstraction import AbstractionUserService
from ..exception import UserNotFound,ProfileNotFound
from ..data_classes import UserDataClass,UsersDataClass,ProfileDataClass
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
            raise UserNotFound(user_id=user_id)
        return UsersDataClass(
            id=get_user.id,
            first_name=get_user.first_name,
            last_name=get_user.last_name
        )
    def create_profile(self, user_id, age, skill_level, position, bio):
        user_profile = self.data_access.create_profile(user_id, age, skill_level, position, bio)
        if not user_profile:
            raise UserNotFound(user_id=user_id)
        return ProfileDataClass(
            id=user_profile.id,
            age=user_profile.age,
            skill_level=user_profile.skill_level,
            position=user_profile.position,
            bio=user_profile.bio,
            created_at=user_profile.created_at
        )
    def get_profile(self,profile_id):
        profile=self.data_access.get_profile(profile_id)
        if not profile:
            raise ProfileNotFound(profile_id=profile_id)
        return ProfileDataClass(
            id=profile.id,
            age=profile.age,
            skill_level=profile.skill_level,
            position=profile.position,
            bio=profile.bio,
            created_at=profile.created_at
        )
    def delete_user(self,user_id):
        deleted_user=self.data_access.delete_user(user_id)
        if not deleted_user:
            raise UserNotFound(user_id=user_id)
        return UsersDataClass(
            id=deleted_user.id,
            first_name=deleted_user.first_name,
            last_name=deleted_user.last_name
        )


from .abstraction import AbstractionService
from ..exception import TeamNotFound
from ..data_classe import MatchDataClass


class Default(AbstractionService):
    def __init__(self,data_access):
        self.data_access=data_access


    def create_team(self,user_id,number_of_player):
        team=self.data_access.create_team(user_id,number_of_player)
        if not team:
            raise TeamNotFound(user_id)
        return MatchDataClass(
            id=team.id,
            user_id=team.user_id,
            number_of_player=team.number_of_player,
            created_at=team.created_at
        )

    
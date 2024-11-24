from .abstraction import AbstractionDataAccess
from project.module.ormsqlachemy import Orm
from project.model.user import User
from project.model.team import Team
class OrmSqlalchemy(AbstractionDataAccess,Orm):

    def create_team(self,user_id,number_of_player):
        team=Team(user_id=user_id
                  ,
                  number_of_player=number_of_player)
        self.add_and_flush(team)
        return team
    def get_team(self,team_id):
        teams=Team.query.filter(Team.id==team_id).first()
        return teams

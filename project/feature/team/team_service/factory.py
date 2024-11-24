from ..setting.development import Development
from ..setting.option import TeamServiceOption
from .default import Default



class FactoryTeamSertvice:
    @staticmethod
    def build_object(data_access,service=Development.TEAM_SERVICE):
        if service == TeamServiceOption.DEFAULT:
            return Default(data_access)
        raise NotImplementedError()
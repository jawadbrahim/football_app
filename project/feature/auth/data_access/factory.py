from ..setting.development import Development
from ..setting.option import OrmSqlalchemyOption
from .ormsqlachemy import OrmSqlAlchemy


class FactoryDataAccess:
    @staticmethod
    def build_object(service=Development.ORM_SQLALCHEMY):
        if service == OrmSqlalchemyOption.ORMSQLALCHEMY:
            return OrmSqlAlchemy()
        raise NotImplementedError()
        
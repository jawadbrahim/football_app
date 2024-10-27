from ..setting.option import OrmSqlalchemyOptiom
from ..setting.development import Development
from .ormsqlalchemy import OrmSqlAlchemy

class FactoryDataAccess:
    @staticmethod
    def build_object(service=Development.ORM_SQLALCHEMY):
        if service ==OrmSqlalchemyOptiom.ORMSQLALCHEMY:
            return OrmSqlAlchemy()
        raise NotImplementedError()
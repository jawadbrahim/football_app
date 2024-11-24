from ..setting.option import OrmSqlalchemyOptiom
from ..setting.development import Development
from .ormsqlachemy import OrmSqlalchemy

class FactoryDataAccess:
    @staticmethod
    def build_object(service=Development.ORM_SQLALCHEMY):
        if service ==OrmSqlalchemyOptiom.ORMSQLALCHEMY:
            return OrmSqlalchemy()
        raise NotImplementedError()
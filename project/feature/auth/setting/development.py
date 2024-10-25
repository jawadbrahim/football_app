from .option import OrmSqlalchemyOption,AuthServiceOption,RequestValidatorOption

class Development:
    ORM_SQLALCHEMY=OrmSqlalchemyOption.ORMSQLALCHEMY
    AUTH_SERVICE=AuthServiceOption.DEFAULT
    REQUEST_VALIDATOR=RequestValidatorOption.PYDANTIC_MODEL
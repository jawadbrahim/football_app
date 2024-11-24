from .option import OrmSqlalchemyOptiom,RequestValidatorOption,TeamServiceOption,ResponseSerializeOption


class Development:
    ORM_SQLALCHEMY=OrmSqlalchemyOptiom.ORMSQLALCHEMY
    TEAM_SERVICE=TeamServiceOption.DEFAULT
    REQUEST_VALIDATOR=RequestValidatorOption.PYDANTIC_MODEL
    RESPONSE_SERIALIZE=ResponseSerializeOption.PYDANTIC_JSON
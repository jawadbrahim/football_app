from .option import OrmSqlalchemyOptiom,RequestValidatorOption,UserServiceOption,ResponseSerializeOption


class Development:
    ORM_SQLALCHEMY=OrmSqlalchemyOptiom.ORMSQLALCHEMY
    USER_SERVICE=UserServiceOption.DEFAULT
    REQUEST_VALIDATOR=RequestValidatorOption.PYDANTIC_MODEL
    RESPONSE_SERIALIZE=ResponseSerializeOption.PYDANTIC_JSON
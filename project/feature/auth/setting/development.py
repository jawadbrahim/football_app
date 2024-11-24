from .option import OrmSqlalchemyOption,AuthServiceOption,RequestValidatorOption,ResponseSerializeOption,GoogleServiceOption

class Development:
    ORM_SQLALCHEMY=OrmSqlalchemyOption.ORMSQLALCHEMY
    AUTH_SERVICE=AuthServiceOption.DEFAULT
    REQUEST_VALIDATOR=RequestValidatorOption.PYDANTIC_MODEL
    RESPONSE_SERIALIZE=ResponseSerializeOption.PYDANTIC_JSON
    GOOGLE_SERVICE=GoogleServiceOption.GOOGLE
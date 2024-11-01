from dataclasses import dataclass
import os
@dataclass
class Development:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    JWT_SECRET=os.getenv("JWT_SECRET")
    JWT_ALGORITHM=os.getenv("JWT_ALGORITHM")

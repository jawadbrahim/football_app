from dataclasses import dataclass
import os
@dataclass
class Development:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:jawadibrahim10@localhost:5432/football_app"

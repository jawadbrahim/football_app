from dataclasses import dataclass
import os
@dataclass
class Development:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    JWT_SECRET=os.getenv("JWT_SECRET")
    JWT_ALGORITHM=os.getenv("JWT_ALGORITHM","HS256")
    GOOGLE_AUTH_CLIENT_ID=os.getenv(
        "GOOGLE_AUTH_CLIENT_ID",
        "37776628693-eujihj10apt0nkjohn56v5gtbamcd9gd.apps.googleusercontent.com"
    )

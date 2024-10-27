from project.config.development import Development
class Config:
    JWT_SECRET=Development.JWT_SECRET
    JWT_ALGORITHM=Development.JWT_ALGORITHM
    JWT_DURATION_IN_MINUTE=60
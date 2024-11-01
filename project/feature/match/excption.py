from project.module.exception_form import AppError

class MatchNotFound(AppError):
    description="match nt found"
    http_code=404
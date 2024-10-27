from project.module.exception_form import AppError

class UserNotFound(AppError):
    description="user not found"
    http_code=404
from project.module.exception_form import AppError

class UserNotFound(AppError):
    description="user not found"
    http_code=404
class EmailAlreadyExist(AppError):
    description="email already exist"
    http_code=404
class CredentialMismatch(AppError):
    description="email or passowrd incorrect"
    http_code=404   
class GoogleAlreadyExist(AppError):
    description="google already exist"
    http_code=404
class InvalidToken(AppError):
    description="token not found"
    http_code=404
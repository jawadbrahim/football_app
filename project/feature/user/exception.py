from project.module.exception_form import AppError

class UserNotFound(AppError):
    description="user not found"
    http_code=404
class ProfileNotFound(AppError):
    description="profile not found"
    http_code=404
class DuplicateProfilrError(AppError):
    description="profile for this user already exist "
    http_code=409
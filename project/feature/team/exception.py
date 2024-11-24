from project.module.exception_form import AppError


class TeamNotFound(AppError):
    description="team not fund"
    http_code=404
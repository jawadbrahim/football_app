from .blueprint import team_bp
from .request_validator import request_validator
from .controller import TeamController


@team_bp.route("/team",methods=["POST"])
@request_validator.validate_create_match()
def create_team(validate_data):
    controller=TeamController()
    response=controller.create_team(validate_data)
    return response,201

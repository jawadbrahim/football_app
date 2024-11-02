from .blueprint import match_bp
from .request_validator import request_validator
from .controller import MatchController

@match_bp.route("/match",methods=["POST"])
@request_validator.validate_create_match()
def create_match(validate_data):
     controller=MatchController()
     response=controller.create_match(validate_data)
     return response,201
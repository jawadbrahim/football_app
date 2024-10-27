from .blueprint import auth_bp
from .request_validator import request_validator
from .controller import AuthController

@auth_bp.route("/register",methods=["POST"])
@request_validator.validate_register()
def register(validate_data):
    controller=AuthController()
    response=controller.register(validate_data)
    return response,201
@auth_bp.route("/login",methods=["POST"])
@request_validator.validate_register()
def login(validate_data):
    controller=AuthController()
    response=controller.login(validate_data)
    return response,201
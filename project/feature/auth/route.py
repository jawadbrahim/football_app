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
@auth_bp.route("/google_status",methods=['POST'])
@request_validator.validate_google()
def google_status(validate_data):
    controller=AuthController()
    response=controller.google_status(validate_data)
    return response,201
@auth_bp.route("/google",methods=["POST"])
@request_validator.validate_google()
def create_google(validate_data):
    controller=AuthController()
    response=controller.create_google(validate_data)
    return response ,201

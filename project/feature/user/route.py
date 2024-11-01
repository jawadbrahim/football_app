from .controller import UserController
from .request_validator import request_validator
from .blueprint import user_bp
from project.decorator.authorization import token_required
@user_bp.route("/user",methods=["POST"])
@request_validator.validate_create_user()
@token_required
def create_user(validate_data):
    controller=UserController()
    response=controller.create_user(validate_data)
    return response,201
@user_bp.route("/user/profile/<uuid:user_id>",methods=["POST"])
@request_validator.valdiate_create_profile()
def create_profile(user_id,validate_data):
    controller=UserController()
    response=controller.create_profile(user_id,validate_data)
    return response,201
@user_bp.route("/user/get_profile/<uuid:profile_id>",methods=["GET"])
def get_profile(profile_id):
    controller=UserController()
    response=controller.get_profile(profile_id)
    return response,201
@user_bp.route("/get_user/<uuid:user_id>",methods=["GET"])
def get_user(user_id):
    controller=UserController()
    response=controller.get_user(user_id)
    return response,201
@user_bp.route("/delete/<uuid:user_id>",methods=["DELETE"])
def delete_user(user_id):
    controller=UserController()
    response=controller.delete_user(user_id)
    return response,201

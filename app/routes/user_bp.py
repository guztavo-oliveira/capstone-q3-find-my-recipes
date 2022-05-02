from flask import Blueprint
from app.controllers import user_controller

bp = Blueprint("user", __name__, url_prefix="/user")

bp.post("")(user_controller.create_user)
bp.post("/login")(user_controller.login)
bp.patch("")(user_controller.update_user)
bp.delete("/<id>")(user_controller.delete_user)

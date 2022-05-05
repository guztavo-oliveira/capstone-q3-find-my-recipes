from flask import Blueprint
from app.controllers import user_controller

bp = Blueprint("user", __name__, url_prefix="/user")

bp.post("")(user_controller.create_user)
bp.post("/login")(user_controller.login)
bp.patch("")(user_controller.update_user)
bp.delete("/<id>")(user_controller.delete_user)
bp.get("")(user_controller.get_all_user_data)
bp.get("/<id>/favorite_recipe")(user_controller.get_user_favorite_recipe)
bp.get("/<id>/recipe_by_user")(user_controller.get_recipe_by_user)
bp.get("/<id>/feed")(user_controller.get_user_feed)

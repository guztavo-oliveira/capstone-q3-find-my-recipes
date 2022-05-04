from flask import Blueprint
from app.controllers import favorites_controller

bp = Blueprint("favorites", __name__, url_prefix="/favorites")

bp.post("")(favorites_controller.post_a_favorite)
bp.delete("/<int:favorite_id>")(favorites_controller.delete_a_favorite)
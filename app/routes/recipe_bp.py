from flask import Blueprint
from app.controllers import recipe_controller

bp = Blueprint("recipe", __name__, url_prefix="/recipe")

bp.get("")(recipe_controller.get_recipes)
bp.post("")(recipe_controller.post_a_recipe)
bp.get("/<post_id>")(recipe_controller.get_a_recipe_by_id)
bp.patch("/<post_id>")(recipe_controller.update_a_recipe)
bp.delete("/<post_id>")(recipe_controller.delete_a_recipe)

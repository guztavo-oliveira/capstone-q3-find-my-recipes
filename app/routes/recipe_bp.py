from flask import Blueprint
from app.controllers import recipe_controller

bp = Blueprint("recipe", __name__, url_prefix="/recipe")

bp.get("")(recipe_controller.get_recipes)
bp.post("")(recipe_controller.post_a_recipe)
bp.get("/type/<category>")(recipe_controller.recipes_by_category)
bp.get("/<recipe_id>")(recipe_controller.get_a_recipe_by_id)
bp.patch("/<recipe_id>")(recipe_controller.update_a_recipe)
bp.delete("/<recipe_id>")(recipe_controller.delete_a_recipe)

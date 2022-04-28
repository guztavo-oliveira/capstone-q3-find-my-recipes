from http import HTTPStatus
from flask import jsonify
from app.configs.database import db
from app.models.recipe_model import RecipeModel

def get_recipes():
    base_query = db.session.query(RecipeModel)
    all_recipes = base_query.order_by(RecipeModel.recipe_id).all()

    return jsonify(all_recipes), HTTPStatus.OK


def get_a_recipe_by_id():
    ...


def post_a_recipe():
    ...


def update_a_recipe(recipe_id):
    ...


def delete_a_recipe(recipe_id):
    ...

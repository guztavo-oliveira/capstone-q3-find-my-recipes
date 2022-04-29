from http import HTTPStatus

from app.configs.database import db
from app.models.recipe_model import RecipeModel, RecipeModelSchema
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import NoResultFound


def get_recipes():
    base_query = db.session.query(RecipeModel)
    all_recipes = base_query.order_by(RecipeModel.recipe_id).all()

    return jsonify(all_recipes), HTTPStatus.OK


def get_a_recipe_by_id(id):
    try:
        recipe = db.session.get(id)

        return RecipeModelSchema.dump(recipe), HTTPStatus.OK
    
    except NoResultFound:
        return {"msg": "recipe does not exist"}, HTTPStatus.NOT_FOUND


@jwt_required()
def post_a_recipe():
    ...


@jwt_required()
def update_a_recipe(recipe_id):
    ...


@jwt_required()
def delete_a_recipe(recipe_id):
    ...

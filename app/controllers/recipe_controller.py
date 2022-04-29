from http import HTTPStatus

from app.configs.database import db
from app.models.recipe_model import RecipeModel, RecipeModelSchema
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from app.exc.user_exc import InvalidKeysError, InvalidValuesError, InvalidUserError
from http import HTTPStatus


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

    valid_keys = [
        "title",
        "time",
        "type",
        "method",
        "status",
        "serves",
        "img_link",
        "user_id",
    ]

    session: Session = db.session
    data = request.get_json()

    user: dict = get_jwt_identity()

    try:
        verify_keys(data, valid_keys)
        send_data = RecipeModel(**data)

        session.add(send_data)
        session.commit()

    except InvalidKeysError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    except InvalidValuesError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    return (
        RecipeModelSchema(
            only=("title", "time", "type", "method", "status", "serves", "img_link")
        ).dump(send_data),
        HTTPStatus.CREATED,
    )


@jwt_required()
def update_a_recipe(recipe_id):
    ...


@jwt_required()
def delete_a_recipe(recipe_id):
    ...


def verify_keys(data: dict, valid_keys):

    invalid_keys = []

    for key, _ in data.items():
        if key not in valid_keys:
            invalid_keys.append(key)

    if invalid_keys:
        raise InvalidKeysError(valid_keys, invalid_keys)

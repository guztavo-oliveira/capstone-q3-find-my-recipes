from http import HTTPStatus

from app.configs.database import db
from app.exc.user_exc import (InsufficienDataKeyError, InvalidEmailError,
                              InvalidKeysError, InvalidUserError,
                              InvalidValuesError)
from app.models.feed_model import FeedModel, FeedModelSchema
from app.models.recipe_model import RecipeModelSchema
from app.models.user_model import UserModel, UserModelSchema
from app.services.validations import (serialize_data,
                                      validate_keys_and_value_type)
from flask import jsonify, request
from flask_jwt_extended import (create_access_token, get_jwt_identity,
                                jwt_required)
from psycopg2.errors import InvalidTextRepresentation, UniqueViolation
from sqlalchemy.exc import DataError, IntegrityError


def create_user():
    valid_keys = ["name", "email", "password"]

    data = request.get_json()

    try:
        if not data:
            raise InsufficienDataKeyError(valid_keys)

        validate_keys_and_value_type(data, valid_keys)

        data["account_type"] = "admin"

        user = UserModel(**data)

        db.session.add(user)
        db.session.commit()

    except InvalidKeysError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    except InvalidValuesError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            return {"msg": "Email already in use!"}, HTTPStatus.BAD_REQUEST
    except InsufficienDataKeyError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    except InvalidEmailError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    return UserModelSchema(only=("name", "email")).dump(user), HTTPStatus.CREATED


def login():
    valid_keys = ["email", "password"]

    try:
        data = request.get_json()
        if not data:
            raise InsufficienDataKeyError(valid_keys)

        validate_keys_and_value_type(data, valid_keys)

        user: UserModel = UserModel.query.filter_by(email=data["email"]).first()

        if not user or not user.check_password(data["password"]):
            raise InvalidUserError

        token = create_access_token(
            UserModelSchema(only=("name", "email", "user_id")).dump(user)
        )

        return {"token": token}

    except InvalidKeysError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    except InvalidValuesError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    except InvalidUserError as e:
        return e.message, HTTPStatus.UNAUTHORIZED

    except InsufficienDataKeyError as e:
        return e.message, HTTPStatus.BAD_REQUEST


@jwt_required()
def update_user():
    valid_keys = ["name", "email", "password"]

    data = request.get_json()
    try:
        if not data:
            raise InsufficienDataKeyError(valid_keys)

        user: UserModel = get_jwt_identity()
        user = UserModel.query.filter_by(email=user["email"]).first()

        validate_keys_and_value_type(data, valid_keys, update=True)

        for key, value in data.items():
            setattr(user, key, value)

        db.session.add(user)
        db.session.commit()

        return UserModelSchema().dump(user), HTTPStatus.OK

    except InvalidKeysError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    except InvalidValuesError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    except InvalidUserError as e:
        return e.message, HTTPStatus.UNAUTHORIZED

    except InsufficienDataKeyError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    except InvalidEmailError as e:
        return e.message, HTTPStatus.BAD_REQUEST


@jwt_required()
def delete_user(id: str):
    try:
        user: UserModel = UserModel.query.filter_by(user_id=id).first()

        if not user:
            return {"msg": "User not found with especified id"}, HTTPStatus.NOT_FOUND

        db.session.delete(user)
        db.session.commit()

        return "", HTTPStatus.NO_CONTENT

    except DataError as e:
        if isinstance(e.orig, InvalidTextRepresentation):
            return {"msg": "Id not valid!"}, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_all_user_data():
    user: UserModel = get_jwt_identity()
    user = UserModel.query.filter_by(user_id=user["user_id"]).first()

    return UserModelSchema().dump(user), HTTPStatus.OK


@jwt_required()
def get_user_favorite_recipe(id: str):
    user = UserModel.query.filter_by(user_id=id).first()

    return jsonify(
        [
            RecipeModelSchema(only=("title",)).dump(item)
            for item in user.recipe_favorites
        ]
    )


@jwt_required()
def get_recipe_by_user(id: str):
    user = UserModel.query.filter_by(user_id=id).first()
    return jsonify(
        [RecipeModelSchema(only=("title",)).dump(item) for item in user.recipe_by_user]
    )


@jwt_required()
def get_user_feed(id: str):
    user = UserModel.query.filter_by(user_id=id).first()

    return jsonify([FeedModelSchema().dump(item) for item in user.feed])


from app.configs.database import db
from flask import jsonify, request, url_for

from ipdb import set_trace
from app.exc.user_exc import (
    InvalidKeysError,
    InvalidValuesError,
    InvalidUserError,
    InsufficienDataKeyError,
    InvalidEmailError,
)
from http import HTTPStatus
from psycopg2.errors import UniqueViolation, InvalidTextRepresentation
from sqlalchemy.exc import IntegrityError, DataError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


from app.models.user_model import UserModel, UserModelSchema
from app.models.recipe_model import RecipeModelSchema
from app.models.feed_model import FeedModel, FeedModelSchema

from app.utils.email_token import generate_confirmation_token, confirm_token
from app.utils.send_email import send_email


def create_user():
    valid_keys = ["name", "email", "password"]

    data = request.get_json()

    try:
        if not data:
            raise InsufficienDataKeyError(valid_keys)

        verify_keys(data, valid_keys)
        data["account_type"] = "admin"

        user = UserModel(**data)

        create_and_send_email(user)

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

        verify_keys(data, valid_keys)

        user: UserModel = UserModel.query.filter_by(email=data["email"]).first()

        if not user or not user.check_password(data["password"]):
            raise InvalidUserError

        if user.confirmed is False:
            return (
                {"message": "The user account is not activated yet"}
            ), HTTPStatus.FORBIDDEN

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

        verify_keys(data, valid_keys, update=True)

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
    set_trace()
    return jsonify(
        [RecipeModelSchema(only=("title",)).dump(item) for item in user.recipe_by_user]
    )


@jwt_required()
def get_user_feed(id: str):
    user = UserModel.query.filter_by(user_id=id).first()

    return jsonify([FeedModelSchema().dump(item) for item in user.feed])


def verify_keys(data: dict, valid_keys, update=False):

    invalid_keys = []

    if not update:
        if len(data) < len(valid_keys):
            raise InsufficienDataKeyError(valid_keys)

    if update:
        for key, value in data.items():
            if key not in tuple(valid_keys):
                raise InvalidKeysError(valid_keys, key)
            if not isinstance(value, str):
                raise InvalidValuesError(key, value)

    for key, value in data.items():
        if key not in valid_keys:
            invalid_keys.append(key)
        if not isinstance(value, str):
            raise InvalidValuesError(key, value)

    if invalid_keys:
        raise InvalidKeysError(valid_keys, invalid_keys)


def create_and_send_email(user: UserModel):
    email_token = generate_confirmation_token(user.email)

    link = url_for("user.validate_user", token=email_token, _external=True)

    send_email(link, user.email, user.name)


def validate_user():
    token = request.args.get("token")
    email = confirm_token(token)

    if email is False:
        return {"msg": "Invalid token or token expired"}, HTTPStatus.BAD_REQUEST

    user: UserModel = UserModel.query.filter_by(email=email).first()

    if not user:
        return {"msg": "User not found"}, HTTPStatus.NOT_FOUND

    if user.confirmed is True:
        return (
            {"msg": "The user account is already activated"},
            HTTPStatus.BAD_REQUEST,
        )

    user.confirmed = True

    db.session.commit()
    return {"msg": "Account verified with success! It's time to  login!"}, HTTPStatus.OK

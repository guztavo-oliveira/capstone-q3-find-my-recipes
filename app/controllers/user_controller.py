from app.configs.database import db
from flask import jsonify, request
from ipdb import set_trace
from app.exc.user_exc import InvalidKeysError
from http import HTTPStatus


from app.models.user_model import UserModel


def create_user():
    data = request.get_json()

    try:

        data["account_type"] = "admin"

        user = UserModel(**data)

        db.session.add(user)
        db.session.commit()

    except InvalidKeysError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    return jsonify(user), HTTPStatus.OK


def login():
    ...


def verify_keys(data: dict):
    valid_keys = ["name", "email", "password"]

    invalid_keys = []

    for key in data:
        if key not in valid_keys:
            invalid_keys.append(key)

    if invalid_keys:
        raise InvalidKeysError(valid_keys, invalid_keys)

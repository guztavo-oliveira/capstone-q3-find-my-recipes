from app.configs.database import db
from flask import jsonify, request
#from ipdb import set_trace
from app.exc.user_exc import InvalidKeysError, InvalidValuesError, InvalidUserError
from http import HTTPStatus
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token


from app.models.user_model import UserModel, UserModelSchema


def create_user():
    valid_keys = ["name", "email", "password"]

    data = request.get_json()

    try:
        verify_keys(data, valid_keys)
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

    return UserModelSchema(only=('name', 'email')).dump(user), HTTPStatus.CREATED


def login():
    valid_keys = ["email", "password"]
    data = request.get_json()
    try:
        verify_keys(data, valid_keys)

        user: UserModel = UserModel.query.filter_by(email=data["email"]).first()

        if not user or not user.check_password(data["password"]):
            raise InvalidUserError

        print('=' * 50)
        print(user)

        token = create_access_token(UserModelSchema(only=("name", "email", "user_id")).dump(user))

        return {"token": token}

    except InvalidKeysError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    except InvalidValuesError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    except InvalidUserError as e:
        return e.message, HTTPStatus.UNAUTHORIZED


def verify_keys(data: dict, valid_keys):

    invalid_keys = []

    for key, value in data.items():
        if key not in valid_keys:
            print(f"{key=}")
            invalid_keys.append(key)
        if not isinstance(value, str):
            raise InvalidValuesError(key, value)

    if invalid_keys:
        raise InvalidKeysError(valid_keys, invalid_keys)

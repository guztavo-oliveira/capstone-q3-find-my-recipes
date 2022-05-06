from datetime import datetime as dt
from http import HTTPStatus

from app.exc.user_exc import InvalidKeysError, InvalidValuesError, InsufficienDataKeyError

from app.configs.database import db
from app.models.feed_model import FeedModel, FeedModelSchema
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm.session import Session

from app.services.validations import validate_keys_and_value_type


@jwt_required()
def get_publications():

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    feed_list = FeedModel.query.paginate(page=page, per_page=per_page)

    return (
        jsonify([FeedModelSchema().dump(items) for items in feed_list.items]),
        HTTPStatus.OK,
    )


@jwt_required()
def get_a_publication(post_id: int):

    publication = FeedModel.query.get(post_id)

    if not publication:
        return {"error": "ID not found"}, HTTPStatus.NOT_FOUND

    return FeedModelSchema().dump(publication), HTTPStatus.OK


@jwt_required()
def post_a_publication():
    try:
        session: Session = db.session

        data = request.get_json()
        user = get_jwt_identity()

        expected_keys = ["publication", "icon"]

        validate_keys_and_value_type(data, expected_keys)

        user_name = user["name"]
        user_id = user["user_id"]

        data = {"user_id": user_id, "user_name": user_name, **data}

        new_feed = FeedModel(**data)

        new_feed.publication_date = dt.now()
        new_feed.user_id = user_id
        new_feed.user_name = user_name

        session.add(new_feed)
        session.commit()

        return FeedModelSchema().dump(new_feed), HTTPStatus.CREATED
    
    except InvalidKeysError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    except InvalidValuesError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    except InsufficienDataKeyError as e:
        return e.message, HTTPStatus.BAD_REQUEST


@jwt_required()
def update_a_publication(post_id: int):
    try:
        data = request.get_json()
        user = get_jwt_identity()

        expected_keys = ["publication", "icon"]

        validate_keys_and_value_type(data, expected_keys)

        feed: FeedModel = FeedModel.query.get(post_id)

        if not feed:
            return {"msg": "Id not found"}, HTTPStatus.NOT_FOUND

        if str(feed.user_id) == user["user_id"]:

            for key, value in data.items():
                setattr(feed, key, value)

            db.session.commit()

            return FeedModelSchema().dump(feed), HTTPStatus.OK

        return {"msg": "Only the owner can make changes"}, HTTPStatus.UNAUTHORIZED

    except InvalidKeysError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    except InvalidValuesError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    except InsufficienDataKeyError as e:
        return e.message, HTTPStatus.BAD_REQUEST


@jwt_required()
def delete_a_publication(post_id: int):

    user = get_jwt_identity()

    feed = FeedModel.query.get(post_id)

    if not feed:
        return {"msg": "Id not found"}, HTTPStatus.NOT_FOUND

    if str(feed.user_id) == user["user_id"]:

        db.session.delete(feed)
        db.session.commit()

        return "", HTTPStatus.NO_CONTENT

    return {"msg": "Only the owner can make changes"}, HTTPStatus.UNAUTHORIZED

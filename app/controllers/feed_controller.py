from datetime import datetime as dt
from http import HTTPStatus

from app.configs.database import db
from app.controllers import valid_key_request
from app.models.feed_model import FeedModel, FeedModelSchema
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm.session import Session


@jwt_required()
def get_publications():

    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    feed_list = FeedModel.query.paginate(page=page, per_page=per_page)

    return jsonify(feed_list.items), HTTPStatus.OK


@jwt_required()
def get_a_publication(post_id:int):
    
    publication = FeedModel.query.get(post_id)
    
    if not publication:
        return {"error": "ID not found"}, HTTPStatus.NOT_FOUND
    
    return FeedModelSchema().dump(publication), HTTPStatus.OK


@jwt_required()
def post_a_publication():

    session: Session = db.session

    data = request.get_json()
    user = get_jwt_identity()

    expected_keys = {'publication', 'icon'}
    required_keys = {'publication'}

    validated =  valid_key_request(data, expected_keys, required_keys )

    if validated:

        return validated, HTTPStatus.BAD_REQUEST

    user_name = user['name']
    user_id = user['user_id']

    data = {'user_id': user_id, 'user_name': user_name, **data}

    new_feed = FeedModel(**data)

    new_feed.publication_date = dt.now()
    new_feed.user_id = user_id
    new_feed.user_name = user_name

    session.add(new_feed)
    session.commit()

    return FeedModelSchema().dump(new_feed), HTTPStatus.CREATED


@jwt_required()
def update_a_publication(post_id: int):

    data = request.get_json()
    user = get_jwt_identity()

    expected_keys = {'publication', 'icon'}
    required_keys = {'publication'}

    validated =  valid_key_request(data, expected_keys, required_keys)

    if validated:

        return validated, HTTPStatus.BAD_REQUEST

    feed: FeedModel = FeedModel.query.get(post_id)

    if not feed:
        return {'msg': 'Id not found'}, HTTPStatus.NOT_FOUND


    if str(feed.user_id) == user['user_id']:

        for key, value in data.items():
            setattr(feed, key, value)
    
        db.session.commit()

        return FeedModelSchema().dump(feed), HTTPStatus.OK

    return {'msg': 'Only the owner can make changes'}, HTTPStatus.UNAUTHORIZED



@jwt_required()
def delete_a_publication(post_id: int):

    user = get_jwt_identity()

    feed = FeedModel.query.get(post_id)

    if not feed:
        return {'msg': 'Id not found'}, HTTPStatus.NOT_FOUND

    if str(feed.user_id) == user['user_id']:

        db.session.delete(feed)
        db.session.commit()

        return '', HTTPStatus.NO_CONTENT

    return {'msg': 'Only the owner can make changes'}, HTTPStatus.UNAUTHORIZED

    
from http import HTTPStatus

from app.configs.database import db
from app.models.feed_model import FeedModel, FeedModelSchema
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm.session import Session
from datetime import datetime as dt


def get_publications():

    feed_list = FeedModel.query.all()

    return jsonify(feed_list), HTTPStatus.OK


@jwt_required()
def post_a_publication():

    session: Session = db.session

    data = request.get_json()
    user = get_jwt_identity()

    user_name = user['name']
    user_id = user['user_id']

    # data = {'user_id': user_id, 'user_name': user_name, **data}

    print('=' * 50)
    print(data)

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

    return ''



@jwt_required()
def delete_a_publication(post_id: int):

    user = get_jwt_identity()

    return ''
    
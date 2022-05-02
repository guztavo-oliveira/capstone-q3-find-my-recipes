from http import HTTPStatus
from app.configs.database import db
from app.controllers.user_controller import verify_keys
from app.models.feed_model import FeedModel, FeedModelSchema
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm.session import Session
from datetime import datetime as dt

@jwt_required()
def get_publications():

    try: 
        per_page = request.args.get("per_page")
        page = request.args.get("page")
        query = FeedModel.query.limit(per_page).offset(page)
        feed_list = query.all()
    
    except:
        feed_list = FeedModel.query.all()

    return FeedModelSchema().dump(feed_list), HTTPStatus.OK

@jwt_required()
def get_a_publication(post_id:int):
    
    publication = FeedModel.query.filter_by(feed_id=post_id).one_or_none()
    
    if publication == None:
        return {"error": "ID inválida"}, HTTPStatus.BAD_REQUEST
    
    return jsonify(publication), HTTPStatus.OK


@jwt_required()
def post_a_publication():

    session: Session = db.session

    data = request.get_json()
    user = get_jwt_identity()

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

    error = verify_keys()

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

    if feed.feed_id == user['user_id']:

        db.session.delete(feed)
        db.session.commit()

        return '', HTTPStatus.NO_CONTENT

    return {'msg': 'Only the owner can make changes'}, HTTPStatus.UNAUTHORIZED

    
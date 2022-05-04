from http import HTTPStatus
from flask import current_app, request
from app.models.favorites_model import FavoritesModel
from app.models.recipe_model import RecipeModel
from app.models.user_model import UserModel
from flask_jwt_extended import get_jwt_identity, jwt_required


@jwt_required()
def post_a_favorite():
    session = current_app.db.session
    data = request.get_json()
    
    recipe_identify = data["recipes_id"]
    user_identify = get_jwt_identity()
    
    recipe = RecipeModel.query.filter_by(recipe_id = recipe_identify).first()
    if not recipe:
        return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND
    

    user = session.query(UserModel).filter(UserModel.user_id  == user_identify["user_id"]).first()
    if not user:
        return {"message": "user not found"}, HTTPStatus.NOT_FOUND

    user.recipe_favorites.append(recipe) 

    session.add(user)
    session.commit()

    return {"message": "successfully added"}, HTTPStatus.OK
    


@jwt_required()
def delete_a_favorite(favorite_id):
  
    session = current_app.db.session
    favorite = session.query(FavoritesModel).get(favorite_id)
    if not favorite:
        return {"error": "id not found"}, HTTPStatus.NOT_FOUND

    session.delete(favorite)
    session.commit()

    return "", HTTPStatus.NO_CONTENT

   




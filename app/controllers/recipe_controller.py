from http import HTTPStatus
from turtle import title
from unicodedata import category, name
from flask import jsonify, request
from ipdb import set_trace
from sqlalchemy import insert
from app.configs.database import db
from app.models.recipe_model import RecipeModel, RecipeModelSchema
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from app.exc.user_exc import InvalidKeysError, InvalidValuesError, InvalidUserError
from http import HTTPStatus
from app.models.ingredient_model import IngredientModel
from app.models.recipe_ingredient_table import RecipeIngredientModel


def get_recipes():
    
        insert_ingredients = [item for item in request.args.get("ingredient").split(",")]
        # Uma lista com os ingredients que quero procurar numa receita

        receita_escolhida = []

        for item in insert_ingredients:   
            
            ingredients_da_receita = IngredientModel.query.filter_by(title=item).first()
            print(ingredients_da_receita.id)

            if ingredients_da_receita:
                receita_escolhida.append(ingredients_da_receita)
            
            # for filtered in ingredients_da_receita:
            #     filtered = base_query.ingredients.filter(name=item).all()

        print(receita_escolhida)

        return jsonify(receita_escolhida)
    
"""     except: 

        base_query = db.session.query(RecipeModel)
        all_recipes = base_query.order_by(RecipeModel.recipe_id).all()
        # return jsonify(all_recipes), HTTPStatus.OK
        return "except" """

def recipes_by_category(category):
    
    try: 
        base_query = db.session.query(RecipeModel)
        recipes = base_query.filter_by(type=category).all()
        return RecipeModelSchema().load(recipes), HTTPStatus.OK
    
    except NoResultFound:
        return {"msg": "category does not exist"}, HTTPStatus.NOT_FOUND


def get_a_recipe_by_id(id):
    try:
        recipe = db.session.get(id)

        return RecipeModelSchema.dump(recipe), HTTPStatus.OK

    except NoResultFound:
        return {"msg": "recipe does not exist"}, HTTPStatus.NOT_FOUND


def create_recipe():
    pass


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
        "ingredients",
    ]

    session: Session = db.session
    data = request.get_json()

    user: dict = get_jwt_identity()

    try:

        verify_keys(data, valid_keys)

        ingredients = data.pop("ingredients")

        data["user_id"] = user["user_id"]

        recipe = RecipeModel(**data)

        for ingredient in ingredients:

            ingredient_name = IngredientModel.query.filter(
                IngredientModel.title.like(f"{ingredient['name']}")
            ).first()

            if not ingredient_name:
                ingredient_name = IngredientModel(title=f"{ingredient['name']}")
                session.add(ingredient_name)
                session.commit()

            recipe.ingredients.append(ingredient_name)

            session.add(recipe)
            session.commit()

            recipe_ingredient = RecipeIngredientModel.query.filter(
                RecipeIngredientModel.ingredient_id == ingredient_name.ingredient_id,
                RecipeIngredientModel.recipe_id == recipe.recipe_id,
            ).first()

            recipe_ingredient.amount = ingredient["amount"]
            recipe_ingredient.unit = ingredient["unit"]

            session.add(recipe_ingredient)
            session.commit()

    except InvalidKeysError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    except InvalidValuesError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    return (
        RecipeModelSchema(
            only=("title", "time", "type", "method", "status", "serves", "img_link")
        ).dump(recipe),
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

from http import HTTPStatus
from flask import jsonify, request
from ipdb import set_trace
from app.configs.database import db
from app.models.recipe_model import RecipeModel, RecipeModelSchema
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from app.exc.user_exc import (
    InvalidKeysError,
    InvalidValuesError,
    InvalidUserError,
    PermissionDeniedError,
)
from http import HTTPStatus
from app.models.ingredient_model import IngredientModel
from app.models.recipe_ingredient_table import RecipeIngredientModel


def get_recipes():

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    base_query = db.session.query(RecipeModel)

    all_recipes = base_query.order_by(RecipeModel.recipe_id).paginate(
        page=page, per_page=per_page
    )

    return (
        jsonify([RecipeModelSchema().dump(recipe) for recipe in all_recipes.items]),
        HTTPStatus.OK,
    )


def get_recipes_by_category(category):

    try:
        base_query = db.session.query(RecipeModel)
        chosen_recipes = base_query.filter_by(type=category).all()
        return (
            jsonify([RecipeModelSchema().dump(recipe) for recipe in chosen_recipes]),
            HTTPStatus.OK,
        )

    except NoResultFound:
        return {"msg": "category does not exist"}, HTTPStatus.NOT_FOUND


def get_a_recipe_by_id(recipe_id: str):
    try:
        recipe = db.session.get(RecipeModel, recipe_id)

        return (
            RecipeModelSchema(exclude=("links", "user_id")).dump(recipe),
            HTTPStatus.OK,
        )
    except NoResultFound:
        return {"msg": "recipe does not exist"}, HTTPStatus.NOT_FOUND


def get_recipe_by_ingredients():

    insert_ingredients = [
        item.strip() for item in request.args.get("ingredient").split(",")
    ]

    ingredients_match_recipes = []
    ingredients_not_match_recipes = []

    # CÓDIGO DO GUSTAVO
    new_recipes = []

    recipes = RecipeModel.query.all()
    print(insert_ingredients)
    for recipe in recipes:
        if all(
            [
                ingredient in [i.title for i in recipe.ingredients]
                for ingredient in insert_ingredients
            ]
        ):
            new_recipes.append(recipe)
    # set_trace()

    teste = [
        {
            "title": recipe.title,
            "time": recipe.time,
            "type": recipe.type,
            "serves": recipe.serves,
            "ingredients": [
                {
                    "title": ingredient.title,
                    "unit": [
                        unit.unit.value
                        for unit in ingredient.unit
                        if unit.recipe_id == recipe.recipe_id
                    ],
                    "amount": [
                        amount.amount
                        for amount in ingredient.amount
                        if amount.recipe_id == recipe.recipe_id
                    ],
                }
                for ingredient in recipe.ingredients
            ],
        }
        for recipe in new_recipes
    ]

    # print(teste)
    set_trace()

    return jsonify(teste)

    # for item in insert_ingredients:
    #     recipe_ingredients = IngredientModel.query.filter_by(title=item).first()
    #     # chamar todas as receitas do banco
    #     # filtrar as receitas por ingrediente
    #     # verificar se pelo um ingrediente esta presente na receita (recipe.ingredient)
    #     # verificar se TODOS os ingredientes estão na receita (filter)
    #     #

    #     if not recipe_ingredients:
    #         ingredients_not_match_recipes.append(item)
    #         continue

    #     for recipe in recipe_ingredients.recipes:
    #         if recipe not in ingredients_match_recipes:
    #             ingredients_match_recipes.append(recipe)

    # page = request.args.get("page", 1, type=int)
    # per_page = request.args.get("per_page", 10, type=int)

    # if ingredients_not_match_recipes:
    #     return {
    #         "recipes found with informed ingredients": [
    #             RecipeModelSchema(
    #                 exclude=("user_id", "status", "recipe_id", "method", "img_link")
    #             ).dump(recipes)
    #             for recipes in ingredients_match_recipes
    #         ],
    #         "ingredients doesn't found in any recipe": [
    #             ingredient for ingredient in ingredients_not_match_recipes
    #         ],
    #     }
    # return {
    #     "recipes found with informed ingredients": [
    #         RecipeModelSchema(
    #             exclude=(
    #                 "user_id",
    #                 "status",
    #                 "recipe_id",
    #                 "method",
    #                 "img_link",
    #             )
    #         ).dump(recipes)
    #         for recipes in ingredients_match_recipes
    #     ][(page - 1) * per_page : page * per_page]
    # }


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
                IngredientModel.title.like(ingredient["title"])
            ).first()

            if not ingredient_name:
                ingredient_name = IngredientModel(title=ingredient["title"])
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
    try:
        data = request.get_json()

        user = get_jwt_identity()

        valid_keys = [
            "title",
            "time",
            "type",
            "method",
            "serves",
            "img_link",
            "ingredients",
        ]

        verify_keys(data, valid_keys)

        recipe_to_update = RecipeModel.query.filter_by(recipe_id=recipe_id).one()

        validate_user(user["user_id"], recipe_to_update.user_id)

        if "ingredients" in data.keys():
            ingredients = data.pop("ingredients")

            for key, value in data.items():
                setattr(recipe_to_update, key, value)

            for ingredient in ingredients:
                ingredient_name = IngredientModel.query.filter(
                    IngredientModel.title.like(ingredient["title"])
                ).first()

                if not ingredient_name:
                    ingredient_name = IngredientModel(title=ingredient["title"])
                    db.session.add(ingredient_name)
                    db.session.commit()

                recipe_to_update.ingredients.append(ingredient_name)

                db.session.add(recipe_to_update)
                db.session.commit()

                recipe_ingredient = RecipeIngredientModel.query.filter(
                    RecipeIngredientModel.ingredient_id
                    == ingredient_name.ingredient_id,
                    RecipeIngredientModel.recipe_id == recipe_to_update.recipe_id,
                ).first()

                recipe_ingredient.amount = ingredient["amount"]
                recipe_ingredient.unit = ingredient["unit"]

                db.session.add(recipe_ingredient)
                db.session.commit()

        return (
            RecipeModelSchema(
                only=("title", "time", "type", "method", "status", "serves", "img_link")
            ).dumps(recipe_to_update),
            HTTPStatus.OK,
        )

    except InvalidKeysError as e:
        return e.message, HTTPStatus.BAD_REQUEST

    except NoResultFound:
        return {"msg": "recipe does not exist"}, HTTPStatus.NOT_FOUND

    except PermissionDeniedError as e:
        return e.message, HTTPStatus.UNAUTHORIZED


@jwt_required()
def delete_a_recipe(recipe_id):
    try:
        session: Session = db.session
        recipe: RecipeModel = RecipeModel.query.filter_by(recipe_id=recipe_id).first()
        session.delete(recipe)
        session.commit()
        return "", HTTPStatus.NO_CONTENT

    except:
        return {"msg": "recipe not found"}, HTTPStatus.NOT_FOUND


def verify_keys(data: dict, valid_keys):

    invalid_keys = []

    for key, _ in data.items():
        if key not in valid_keys:
            invalid_keys.append(key)

    if invalid_keys:
        raise InvalidKeysError(valid_keys, invalid_keys)


def validate_user(jwt_user_id, recipe_user_id):
    if jwt_user_id != str(recipe_user_id):
        raise PermissionDeniedError

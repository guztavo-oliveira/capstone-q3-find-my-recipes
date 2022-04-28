import enum

from app.configs.database import db
from app.exc.recipe_ingredient_exc import InvalidAmount, InvalidUnit
from marshmallow import Schema, fields
from sqlalchemy import Column, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import validates


class RecipeIngredientSchema(Schema):
    recipe_ingredient_id = fields.Int()
    recipe_id = fields.Int()
    ingredient_id = fields.Int()
    unit = fields.Str()
    amount = fields.Float()


class UnitEnum(enum.Enum):
    QUILO = "kg"
    GRAMA = "g"
    LITRO = "l"
    MILILITRO = "ml"
    XICARA = "xícara"
    COLHER = "colher"
    UNIDADE = "unidade"


class RecipeIngredientModel(db.Model):

    __tablename__ = "recipe_ingredient"

    recipe_ingredient_id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey("recipes.recipe_id"), nullable=False)
    ingredient_id = Column(
        Integer, ForeignKey("ingredient.ingredient_id"), nullable=False
    )
    unit = Column(Enum(UnitEnum), nullable=False)
    amount = Column(Float, nullable=False)


@validates("unit")
def validate_unit(self, __, unit_to_test):
    if type(unit_to_test) != str:
        raise InvalidUnit
    return unit_to_test


@validates("amount")
def validate_amount(self, __, amount_to_test):
    if type(amount_to_test) != float:
        raise InvalidAmount
    return amount_to_test

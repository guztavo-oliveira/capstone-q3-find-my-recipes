from app.configs.database import db
from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .recipe_ingredient_table import RecipeIngredientSchema

# from .recipe_model import RecipeModel


class IngredientSchema(Schema):
    class Meta:
        ordered = True

    ingredient_id = fields.Int()
    title = fields.Str()
    unit = fields.Pluck(RecipeIngredientSchema, "unit", many=True)
    # amount = fields.List(fields.Nested(RecipeIngredientSchema))

    amount = fields.Pluck(RecipeIngredientSchema, "amount", many=True)


class IngredientModel(db.Model):

    __tablename__ = "ingredient"

    ingredient_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)

    recipes = relationship(
        "RecipeModel", secondary="recipe_ingredient", back_populates="ingredients"
    )

    unit = relationship("RecipeIngredientModel")
    # unit = relationship(
    # "RecipeIngredientModel",
    # primaryjoin="foreign(RecipeIngredientModel.recipe_id) == remote(foreign(RecipeModel.recipe_id)) ",
    # foreign_keys=["IngredientModel.ingredient_id"],
    # primaryjoin="remote(RecipeModel.recipe_id) == (RecipeIngredientModel.recipe_id)",
    # viewonly=True,
    # )
    amount = relationship("RecipeIngredientModel")

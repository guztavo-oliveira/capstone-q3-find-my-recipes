from app.configs.database import db
from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# from .recipe_model import RecipeModel


class IngredientSchema(Schema):
    ingredient_id = fields.Int()
    title = fields.Str()
    # recipes = fields.List(fields.Nested(RecipeModel))


class IngredientModel(db.Model):

    __tablename__ = "ingredient"

    ingredient_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)

    recipes = relationship(
        "RecipeModel", secondary="recipe_ingredient", back_populates="ingredients"
    )

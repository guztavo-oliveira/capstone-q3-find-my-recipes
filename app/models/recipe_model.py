import enum
from uuid import uuid4

from app.configs.database import db
from marshmallow import Schema, fields
from sqlalchemy import Column, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .recipe_ingredient_table import RecipeIngredientModel


class MyEnum(enum.Enum):
    NOT_VERIFIED = 0
    VERIFIED = 1


class RecipeModelSchema(Schema):
    recipe_id = fields.Int()
    title = fields.Str()
    time = fields.Str()
    type = fields.Str()
    method = fields.Str()
    status = fields.Str()
    serves = fields.Int()
    img_link = fields.Str()
    user_id = fields.Int()


class RecipeModel(db.Model):

    __tablename__ = "recipes"

    recipe_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    time = Column(String, nullable=False)
    type = Column(String, nullable=False)
    method = Column(Text, nullable=False)
    status = Column(Enum(MyEnum), nullable=False)
    serves = Column(Integer, nullable=False)
    img_link = Column(String, nullable=False)

    user_id = Column(UUID(as_uuid=True), ForeignKey("user.user_id"), default=uuid4)

    user = relationship("UserModel", back_populates="recipe_favorites")

    ingredients = relationship(
        "IngredientModel", secondary="recipe_ingredient", back_populates="recipes"
    )

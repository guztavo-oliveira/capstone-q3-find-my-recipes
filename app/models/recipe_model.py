import enum
from uuid import uuid4

from app.configs.database import db
from marshmallow import Schema, fields
from sqlalchemy import Column, Enum, ForeignKey, Integer, String, Text, values
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .recipe_ingredient_table import RecipeIngredientModel
from .ingredient_model import IngredientSchema
from flask_marshmallow.fields import Hyperlinks, URLFor


class MyEnum(enum.Enum):
    NOT_VERIFIED = 0
    VERIFIED = 1


class RecipeModelSchema(Schema):
    class Meta:
        ordered = True

    recipe_id = fields.Int()
    title = fields.Str()
    time = fields.Str()
    type = fields.Str()
    method = fields.Str()
    status = fields.Str()
    serves = fields.Int()
    img_link = fields.Str()
    user_id = fields.Int()
    ingredients = fields.List(fields.Nested(IngredientSchema))

    links = Hyperlinks(
        {
            "Show more": URLFor(
                "recipe.get_a_recipe_by_id", values=dict(recipe_id="<recipe_id>")
            )
        }
    )


class RecipeModel(db.Model):

    __tablename__ = "recipes"

    recipe_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    time = Column(String, nullable=False)
    type = Column(String, nullable=False)
    method = Column(Text, nullable=False)
    status = Column(Enum(MyEnum), nullable=False, default="NOT_VERIFIED")
    serves = Column(Integer, nullable=False)
    img_link = Column(String, nullable=False)

    user_id = Column(UUID(as_uuid=True), ForeignKey("user.user_id"), default=uuid4)
    made_by_user = relationship("UserModel", back_populates="recipe_by_user")
    ingredients = relationship(
        "IngredientModel", secondary="recipe_ingredient", back_populates="recipes"
    )

    def __repr__(self):
        # return "<Recipe %r>" % (self.title)
        return f"<Recipe {self.title}'>"

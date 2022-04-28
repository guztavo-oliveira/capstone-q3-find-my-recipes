from app.configs.database import db
from marshmallow import Schema, fields
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID


class FavoritesSchema(Schema):
    favorite_id = fields.Int()
    user_id = fields.Int()
    recipes_id = fields.Int()

class FavoritesModel(db.Model):
    __tablename__ = "favorites"

    favorite_id = Column(Integer, primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.user_id"), nullable=False)
    reciped_id = Column(Integer, ForeignKey("recipes.recipe_id"), nullable=False)
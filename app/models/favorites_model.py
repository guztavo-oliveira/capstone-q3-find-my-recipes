from app.configs.database import db
from marshmallow import Schema, fields
from sqlalchemy import Column, ForeignKey, Integer


class FavoritesSchema(Schema):
    favorite_id = fields.Int()
    user_id = fields.Int()
    # reciped_id = fields.Int()

class FavoritesModel(db.Model):
    __tablename__ = "favorites"

    favorite_id: int 
    user_id: int  
    # reciped_id: int

    favorite_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    # reciped_id: Column(Integer, ForeignKey("reciped.recipe_id"), nullable=False)
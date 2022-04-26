from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String



@dataclass
class IngredientModel(db.Model):
    ingredient_id = int
    title = str

    __tablename__ = "ingredient"

    ingredient_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    quantity_id = Column(
        Integer, 
        ForeignKey("quantity.quantity_id"), 
        nullable=False)

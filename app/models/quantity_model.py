from dataclasses import dataclass
from app.configs.database import db
import enum
from sqlalchemy import Column, Integer, Enum
from sqlalchemy.orm import validates
from app.exc.quantity_exc import InvalidUnit

class MyEnum(enum.Enum):
    QUILO = "kg" 
    GRAMA = "g"
    LITRO = "l"
    MILILITRO = "ml"
    XICARA = "xícara"

@dataclass
class QuantityModel(db.Model):
    
    __tablename__ = "quantity"

    quantity_id: int 
    unit: str  
    amount: int # Equivalente ao peso para os alimentos e ao volume para os líquidos

    quantity_id = Column(Integer, primary_key=True)
    unit = Column(Enum(MyEnum), nullable=False)
    amount = Column(Integer, nullable=False)

@validates("unit")
def validate_unit(self, __, unit_to_test):
    if type(unit_to_test) != str:
        raise InvalidUnit
    return unit_to_test
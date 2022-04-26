from email.policy import default
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


@dataclass
class UserModel(db.Model):

    __tablename__ = "user"

    user_id: int
    name: str
    email: str
    account_type: str

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    account_type = Column(String, nullable=False)

    # Relationship to bring back the recipes favorited by the user
    # favorites = relationship("recipe_model", secondary='favorites')

    @property
    def password(self):
        raise AttributeError("Not authorized to access")

    @password.setter
    def password(self, pass_to_hash):
        self.password_hash = generate_password_hash(pass_to_hash)

    def check_password(self, pass_to_check):
        return check_password_hash(self.password_hash, pass_to_check)

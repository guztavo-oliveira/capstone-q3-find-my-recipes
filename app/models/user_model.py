from app.configs.database import db
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, validates
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from marshmallow import Schema, fields
from app.models.recipe_model import RecipeModel, RecipeModelSchema
from flask_marshmallow.fields import Hyperlinks, URLFor
import re
from app.exc.user_exc import InvalidEmailError


class UserModelSchema(Schema):
    class Meta:
        ordered = True

    user_id = fields.Str()
    name = fields.Str()
    email = fields.Str()

    links = Hyperlinks(
        {
            "recipes": URLFor(
                "user.get_recipe_by_user",
                values=dict(id="<user_id>"),
            ),
            "favorites_recipes": URLFor(
                "user.get_user_favorite_recipe",
                values=dict(id="<user_id>"),
            ),
            "feed": URLFor("user.get_user_feed", values=dict(id="<user_id>")),
        }
    )


class UserModel(db.Model):

    __tablename__ = "user"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    account_type = Column(String, nullable=False)

    recipe_favorites = relationship("RecipeModel", secondary="favorites")
    recipe_by_user = relationship("RecipeModel", back_populates="made_by_user")
    feed = relationship("FeedModel", back_populates="user")

    @property
    def password(self):
        raise AttributeError("Not authorized to access")

    @password.setter
    def password(self, pass_to_hash):
        self.password_hash = generate_password_hash(pass_to_hash)

    def check_password(self, pass_to_check):
        return check_password_hash(self.password_hash, pass_to_check)

    @validates("name", "email")
    def validate_fields(self, key, value):
        if key == "email":
            email_regex = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

            if not re.fullmatch(email_regex, value):
                raise InvalidEmailError

        return value.lower()

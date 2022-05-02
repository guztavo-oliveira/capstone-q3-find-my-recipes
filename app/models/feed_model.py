from datetime import datetime as dt
from uuid import uuid4

from app.configs.database import db
from marshmallow import Schema, fields
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID


class FeedModelSchema(Schema):
    feed_id = fields.Int()
    icon = fields.Str()
    user_name = fields.Str()
    publication_date = fields.Str()
    publication = fields.Str()


class FeedModel(db.Model):

    __tablename__ = "feed"

    feed_id = Column(BigInteger, primary_key=True)
    icon = Column(String)
    user_name = Column(String, nullable=False)
    publication_date = Column(DateTime, default=dt.now())
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.user_id"), default=uuid4)
    publication = Column(Text, nullable=False)

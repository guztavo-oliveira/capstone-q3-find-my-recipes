from flask import Flask
from flask_migrate import Migrate
from app.configs.database import db


def init_app(app: Flask):
    Migrate(app=app, db=app.db)

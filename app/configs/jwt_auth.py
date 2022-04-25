from os import getenv
from flask_jwt_extended import JWTManager

from flask import Flask


def init_app(app: Flask):
    app.config["JWT_SECRET_KEY"] = getenv("SECRET")
    JWTManager(app)

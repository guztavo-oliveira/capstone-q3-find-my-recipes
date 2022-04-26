from flask import Flask
from .user_bp import bp as user_bp


def init_app(app: Flask):
    app.register_blueprint(user_bp)

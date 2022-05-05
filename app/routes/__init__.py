from flask import Flask
from .user_bp import bp as user_bp
from .feed_bp import bp as feed_bp
from .recipe_bp import bp as recipe_bp
from .favorites_bp import bp as favorites_bp


def init_app(app: Flask):
    app.register_blueprint(user_bp)
    app.register_blueprint(feed_bp)
    app.register_blueprint(recipe_bp)
    app.register_blueprint(favorites_bp)

from flask import Flask
from .user_bp import bp as user_bp
from .feed_bp import bp as feed_bp

def init_app(app: Flask):
    app.register_blueprint(user_bp)
    app.register_blueprint(feed_bp)
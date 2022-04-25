from flask import Flask
from dotenv import load_dotenv
from app.configs import database, migration, jwt_auth
from app import routes

load_dotenv()


def create_app():
    app = Flask(__name__)

    database.init_app(app)
    migration.init_app(app)
    jwt_auth.init_app(app)
    routes.init_app(app)

    return app

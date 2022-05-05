from flask import Flask
from dotenv import load_dotenv
from app.configs import database, migration, jwt_auth, email
from app import routes

from app.admin import admin
from app.admin.admin_user import UserAdmin
from app.admin.recipe_admin import RecipeAdmin
from app.models.user_model import UserModel
from app.models.recipe_model import RecipeModel

from os import getenv

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["FLASK_ADMIN_SWATCH"] = "cerulean"
    app.config["SECRET_KEY"] = getenv("SECRET")

    database.init_app(app)
    migration.init_app(app)
    jwt_auth.init_app(app)
    admin.init_app(app)
    admin.add_view(UserAdmin(UserModel, app.db.session))
    admin.add_view(RecipeAdmin(RecipeModel, app.db.session))
    # email.init_app(app)
    routes.init_app(app)

    return app

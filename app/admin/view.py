from . import admin
from .admin_user import UserAdmin
from app.configs.database import db
from app.models.user_model import UserModel


admin.add_view(UserAdmin(UserAdmin(UserModel, db.session)))

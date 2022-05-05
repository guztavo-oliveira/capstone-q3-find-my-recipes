from flask_admin.contrib.sqla import ModelView
from app.models.user_model import UserModel


class UserAdmin(ModelView):
    # column_list = ("name", "email", "account_type")
    column_exclude_list = "password_hash"

    # form_columns = ("name", "email")

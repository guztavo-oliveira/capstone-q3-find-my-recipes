from flask import Flask
from flask_admin import Admin


admin = Admin()


def init_app(app: Flask):
    admin.init_app(app, name="Find my recipe", template_mode="bootstrap2")

from flask import current_app
from itsdangerous import URLSafeTimedSerializer
from os import getenv


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    return serializer.dumps(email, salt=getenv("EMAIL_SALT"))


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    try:
        email = serializer.loads(token, salt=getenv("EMAIL_SALT"), max_age=expiration)

    except:
        return False
    return email

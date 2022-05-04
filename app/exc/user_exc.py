class InvalidKeysError(Exception):
    def __init__(self, valid_keys, invalid_keys):
        self.message = {"msg": {"valid_keys": valid_keys, "invalid_keys": invalid_keys}}


class InvalidValuesError(Exception):
    def __init__(self, key, value):
        self.message = {"msg": f"item {key}: {value} must be a string"}


class InvalidUserError(Exception):
    def __init__(self):
        self.message = {"msg": "Invalid email or password!"}


class InsufficienDataKeyError(Exception):
    def __init__(self, valid_keys):
        self.message = {
            "msg": f"Insufficient keys! Must be at least this keys {valid_keys}"
        }

class PermissionDeniedError(Exception):
    def __init__(self):
        self.message = {"msg": "You are not allowed to execute this action"}

class InvalidEmailError(Exception):
    def __init__(self):
        self.message = {"msg": "Invalid email!"}

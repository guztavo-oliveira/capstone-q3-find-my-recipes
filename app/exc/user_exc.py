class InvalidKeysError(Exception):
    def __init__(self, valid_keys, invalid_keys):
        self.message = {"msg": {"valid_keys": valid_keys, "invalid_keys": invalid_keys}}


class InvalidValuesError(Exception):
    def __init__(self, key, value):
        self.message = {"msg": f"item {key}: {value} must be a string"}


class InvalidUserError(Exception):
    def __init__(self):
        self.message = {"msg": "Invalid email or password!"}
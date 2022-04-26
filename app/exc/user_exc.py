class InvalidKeysError(Exception):
    def __init__(self, valid_keys, invalid_keys):
        self.message = {"valid_keys": valid_keys, "invalid_keys": invalid_keys}

from app.exc.user_exc import InvalidValuesError, InsufficienDataKeyError, InvalidKeysError

def serialize_data(data: dict):
    for key, value in data.items():
        if key == "status" or "unit":
            data[key] = value.upper()
        elif isinstance(value, str):
            data[key] = value.lower()


def validate_keys_and_value_type(data: dict, valid_keys, update=False):
    for key, value in data.items():
        if key not in valid_keys:
            invalid_keys.append(key)

        if key == "serves":
            if not isinstance(value, int):
                raise InvalidValuesError(key, value)

        else:
            if not isinstance(value, str):
                raise InvalidValuesError(key, value)

    invalid_keys = []

    if update:
        for key, value in data.items():
            if key not in tuple(valid_keys):
                raise InvalidKeysError(valid_keys, key)

    else:
        if len(data) < len(valid_keys):
            raise InsufficienDataKeyError(valid_keys)
        

    if invalid_keys:
        raise InvalidKeysError(valid_keys, invalid_keys)

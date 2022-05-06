from app.exc.user_exc import InvalidValuesError, InsufficienDataKeyError, InvalidKeysError

def serialize_data(data: dict):
    for key, value in data.items():
        if key == "status" or key == "unit":
            data[key] = value.upper()
        elif isinstance(value, str):
            data[key] = value.lower()


def validate_keys_and_value_type(data: dict, valid_keys, update=False):
     invalid_keys = []

     for key, value in data.items():
        if key not in valid_keys:
            invalid_keys.append(key)

        if key == "serves":
            if not isinstance(value, int):
                raise InvalidValuesError(key, value)

        elif key == "ingredients":
            if not isinstance(value, list):
                raise InvalidValuesError(key, value)
            
            else:
                for item in value:
                    print(item)
                    if not isinstance(item, dict):
                        raise InvalidValuesError
                    for k, v in item.items():
                        if k == "amount":
                            if not isinstance(v, int) and not isinstance(v, float):
                                raise InvalidValuesError(k, v)
                        else:
                            if not isinstance(v, str):
                                raise InvalidValuesError(k, v)

        else:
            if not isinstance(value, str):
                raise InvalidValuesError(key, value)

        if update:
            for key, value in data.items():
                if key not in tuple(valid_keys):
                    raise InvalidKeysError(valid_keys, key)

        else:
            if len(data) < len(valid_keys):
                raise InsufficienDataKeyError(valid_keys)
            

        if invalid_keys:
            raise InvalidKeysError(valid_keys, invalid_keys)

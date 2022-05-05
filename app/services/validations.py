from app.exc.user_exc import InvalidValuesError

def serialize_data(data: dict):
    for key, value in data.items():
        if key == "status" or "unit":
            data[key] = value.upper()
        elif isinstance(value, str):
            data[key] = value.lower()


def validate_value_type(data: dict):
    for key, value in data.items():
        if key == "serves":
            isinstance(value, int)
        else:
            isinstance(value, str)

        # fazer raise do invalid values
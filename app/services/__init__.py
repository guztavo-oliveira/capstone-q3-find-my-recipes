def serialize_data(data: dict):
    for key, value in data.items():
        if key == "status" or "unit":
            data[key] = value.upper()
            ...
        elif isinstance(value, str):
            data[key] = value.lower()

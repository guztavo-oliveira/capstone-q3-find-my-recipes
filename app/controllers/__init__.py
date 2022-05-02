
def valid_key_request(request: dict, expected_keys: set, required_keys: set):

    set_request_keys = set(request.keys())
    keys_not_found = required_keys - set_request_keys
    invalid_key = set_request_keys - expected_keys

    if keys_not_found and invalid_key:

        return {
            'error': 'There are invalid and missing keys in your request',
            'required_keys': list(required_keys),
            'keys_not_found': list(keys_not_found),
            'invalid_key': list(invalid_key)
        }
    
    if keys_not_found:

        return {
            'error': 'There are missing keys in your request',
            'required_keys': list(required_keys),
            'keys_not_found': list(keys_not_found)
        }

    if invalid_key:

        return {
            'error': 'There are invalid keys in your request',
            'required_keys': list(required_keys),
            'invalid_key': list(invalid_key)
        }



def _dict_types(value, parsed_type):
    # Kontrola pro Dict

    if "dict" in parsed_type:

        if not isinstance(value, dict):
            return False

        if parsed_type["dict"] == ("Any", "Any"):
            return True

        key_type, value_type = parsed_type["dict"]
        return all(
            validate_value(k, key_type) and validate_value(v, value_type)
            for k, v in value.items()
        )
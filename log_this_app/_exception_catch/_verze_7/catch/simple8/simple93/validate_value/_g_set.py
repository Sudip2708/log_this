

def _set_types(value, parsed_type):
    # Kontrola pro Set

    if "set" in parsed_type:

        if not isinstance(value, set):
            return False

        if parsed_type["set"] == "Any":
            return True

        return all(
            validate_value(item, parsed_type["set"])
            for item in value
        )
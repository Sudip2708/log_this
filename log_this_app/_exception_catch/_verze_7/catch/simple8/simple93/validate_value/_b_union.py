

def _union_types(value, parsed_type):
    # Kontrola pro Union

    if "union" in parsed_type:

        return any(validate_value(value, arg) for arg in parsed_type["union"])
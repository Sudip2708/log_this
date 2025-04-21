

def _optional_types(value, parsed_type):
    # Kontrola pro Optional

    if "optional" in parsed_type:

        return value is None or validate_value(value, parsed_type["optional"])
# Jednoduchý přístup se slovníkem
TYPE_VALIDATORS = {
    list: {
        'validate_type': lambda value: isinstance(value, list),
        'validate_items': lambda value, item_type, deep_check: all(
            verify(item, item_type, deep_check) for item in value)
    },
    # další typy...
}


def verify(value, expected_type, deep_check=True):
    origin = get_origin(expected_type) or expected_type

    if origin in TYPE_VALIDATORS:
        validator = TYPE_VALIDATORS[origin]

        if not validator['validate_type'](value):
            raise TypeError(f"Očekáván typ {origin}, obdržen {type(value)}")

        if deep_check and get_args(expected_type):
            return validator['validate_items'](value, *get_args(expected_type),
                                               deep_check)

        return True
    # fallback...
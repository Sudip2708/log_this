

def _mapping_types(value, type_name, type_args):
    # Kontrola pro Sequence

    if type_name == "mapping":

        if not isinstance(value, Mapping):
            return False

        if type_args == ("Any", "Any"):
            return True

        key_type, value_type = type_args
        return all(
            validate_value(k, key_type)
            and validate_value(v, value_type)
            for k, v in value.items()
        )
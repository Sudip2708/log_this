

def _sequence_types(value, type_name, type_args):
    # Kontrola pro Sequence

    if type_name == "sequence":

        if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
            return False

        if type_args == "Any":
            return True

        return all(validate_value(item, type_args) for item in value)
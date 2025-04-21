

def _base_types(value, parsed_type):
    # Kontrola pro základní typy (str, int, bool, atd.)

    if isinstance(parsed_type, str):
        if parsed_type == "Any":
            return True

        if parsed_type == "None" and value is None:
            return True

        try:

            type_class = eval(parsed_type)
            return isinstance(value, type_class)

        except (NameError, SyntaxError):
            return str(type(value).__name__) == parsed_type
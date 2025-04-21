

def _literal_types(value, parsed_type):
    # Kontrola pro Literal

    if "literal" in parsed_type:

        return value in parsed_type["literal"]
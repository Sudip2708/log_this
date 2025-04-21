

def check_type(value, type_annotation):
    """
    Zkontroluje, zda hodnota odpovídá dané typové anotaci.

    Args:
        value: Hodnota k ověření
        type_annotation: Typová anotace (např. List[str], Union[int, str], atd.)

    Returns:
        bool: True, pokud hodnota odpovídá typové anotaci, jinak False
    """
    parsed_type = parse_typing_annotation(type_annotation)
    return validate_value(value, parsed_type)
def validate_list_arguments(args):
    """Zkontroluje, zda seznam obsahuje pouze dvojice (style, text)"""
    if not isinstance(args, list) or not all(
            isinstance(item, tuple) and len(item) == 2 for item in args):
        raise ValueError("List must contain only tuples of (style, text)")
from typing import Required, get_origin, TypedDict


def check_required_keys(base_dict, value_dict, bool_only=False):
    """Pomocná funkce pro TypedDict"""

    # Ověření že se jedná o TypedDict
    if not hasattr(base_dict, '__total__'):
        raise NotTypedDictError()

    try:

        # Načtení povynných klíčů
        required_keys = {
            k for k, v in base_dict.items()
            if get_origin(v) is Required
        }

        # Zjištění chybějících povinných klíčů
        missing = required_keys - set(value_dict.keys())

        # Pokud chybý některé
        if missing:

            # Pokud je žádost na bool odpověď
            if bool_only:
                return False

            # Jinak vyhlaš výjimku (potřeba dopsat)
            raise MyKeyError(missing=missing)

        return True

    # Dopsat zachytávání neplatných vstupů
    except TypeError as e:
        raise MyTypeError()

    # Dopsat zachytávání neočekávaných výjimek
    except Exception as e:
        raise

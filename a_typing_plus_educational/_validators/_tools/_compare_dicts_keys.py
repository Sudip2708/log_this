
def compare_dicts_keys(base_dict, value_dict, bool_only=False):
    """Pomocná funkce pro TypedDict"""
    try:

        # Načtení množin s klíčy
        expected_keys = set(base_dict.keys())
        actual_keys = set(value_dict.keys())

        # Porovnání zda nějaké klíče nechybí a nebo nepřebívají
        missing = expected_keys - actual_keys
        extra = actual_keys - expected_keys

        # Ošetření nerovností
        if missing or extra:

            # Pokud je žádost na bool odpověď
            if bool_only:
                return False

            # Jinak vyhlaš výjimku (potřeba dopsat)
            raise MyKeyError(missing, extra)

        return True

    # Dopsat zachytávání neplatných vstupů
    except TypeError as e:
        raise MyTypeError()

    # Dopsat zachytávání neočekávaných výjimek
    except Exception as e:
        raise

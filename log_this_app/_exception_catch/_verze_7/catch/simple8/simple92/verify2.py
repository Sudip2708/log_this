from typing import TypeVar, get_origin, get_args


def _verify_python_type(value, expected_type, deep_check=True):
    """Ověří, zda hodnota odpovídá očekávanému typu."""

    # Ověření pravdivosti
    if isinstance(value, expected_type):
        return True

    # Vyvolání výjimky pokud se ověření nepvedlo
    raise TypeError(f"Očekáván typ {expected_type}, obdržen {type(value)}")



def verify(value, expected_type, deep_check=True):
    """Ověří, zda hodnota odpovídá očekávanému typu, včetně generických typů."""

    # Ověří typu (je-li expected_type předáno jako typ)
    if isinstance(expected_type, type):
        _verify_python_type(value, expected_type)

    # Ověří generického typu (je-li expected_type předáno jako generický typ)
    if get_origin(expected_type) is not None:
        _verify_typing_type(value, expected_type)

    else:
        # Vymyslet logiku pro vyřízení ostatních jako Union atd
        pass

    # Pokud ani jeedno ověření není pravdivé (nejedná se o typ ani generický typ)
    raise TypeError(f"Neplatný typ pro ověření: {expected_type}")

# value = {"some_key": "some_text"}
# expected_type = Dict[str, str]


def _verify_typing_type(value, expected_type, deep_check=True):
    """Ověří, zda hodnota odpovídá očekávanému generickému typu."""

    # Načtení typu
    origin_type = get_origin(expected_type)

    # Načtení klíče
    type_name = origin_type.__name__.lower()

    # Načtení třídy pro daný typ
    type_class = VALIDATORS[type_name]

    # Načtení metody pro ověření instance
    validate_type = type_class.validate_type

    # Ověření typu
    if not validate_type(value, origin_type):
        raise TypeError(f"Očekáván typ {origin_type}, obdržen {type(value)}")

    # Ověření, zda se má kontrolovat i vnitřní obsah
    if deep_check == 0:  # 0 nebo False deklarují že se vnitřních obsah nemá kontrolovat
        return True  # V takovou chvíli je ověření úspěšné a u konce

    # Změna hodnoty deep_check:
    if deep_check is not True:
        deep_check -= 1

    # Načtení metody pro ověření vnitřních položek
    validate_items = type_class.validate_items

    # Použití metody pro ověření pravdivosti
    validate_items(value, expected_type, deep_check)




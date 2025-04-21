from typing import get_origin, get_args, Union, List, Dict, Set, Tuple, Any, \
    Optional


def verify_generic_type(value, expected_type):
    """Ověří, zda hodnota odpovídá očekávanému generickému typu."""

    # Získání původního typu (např. list z List[int])
    origin = get_origin(expected_type)

    # Pokud nejde o generický typ, končíme
    if origin is None:
        return False

    # Získání argumentů (např. int z List[int])
    args = get_args(expected_type)

    # Ověření kontejneru
    if not isinstance(value, origin):
        raise TypeError(f"Očekáván kontejner {origin}, obdržen {type(value)}")

    # Speciální zpracování podle typu kontejneru
    if origin is list or origin is List:
        _verify_list_elements(value, args)
    elif origin is dict or origin is Dict:
        _verify_dict_elements(value, args)
    elif origin is set or origin is Set:
        _verify_set_elements(value, args)
    elif origin is tuple or origin is Tuple:
        _verify_tuple_elements(value, args)
    elif origin is Union:
        _verify_union_type(value, args)
    elif origin is Optional:
        _verify_optional_type(value, args)
    # Další typy kontejnerů by se přidaly zde...
    else:
        # Pro neznámé kontejnery alespoň ověříme základní typ
        if not isinstance(value, origin):
            raise TypeError(f"Očekáván typ {origin}, obdržen {type(value)}")

    return True


def _verify_list_elements(value, args):
    """Ověří prvky seznamu."""
    # Pro prázdný seznam není co ověřovat
    if not value:
        return

    # Typ prvků seznamu (první argument)
    elem_type = args[0]

    # Ověření každého prvku
    for i, item in enumerate(value):
        try:
            # Rekurzivní ověření - buď jako obyčejný typ nebo generický
            if not verify_type(item, elem_type) and not verify_generic_type(
                    item, elem_type):
                raise TypeError(
                    f"Prvek na indexu {i} neodpovídá typu {elem_type}")
        except TypeError as e:
            # Přidáme kontext, kde k chybě došlo
            raise TypeError(f"Chyba v seznamu na indexu {i}: {str(e)}")


def _verify_dict_elements(value, args):
    """Ověří prvky slovníku."""
    # Pro prázdný slovník není co ověřovat
    if not value:
        return

    # Typy klíčů a hodnot
    key_type, val_type = args

    # Ověření každého klíče a hodnoty
    for k, v in value.items():
        try:
            # Ověření klíče
            if not verify_type(k, key_type) and not verify_generic_type(k,
                                                                        key_type):
                raise TypeError(f"Klíč {k} neodpovídá typu {key_type}")
        except TypeError as e:
            raise TypeError(f"Chyba v klíči slovníku {k}: {str(e)}")

        try:
            # Ověření hodnoty
            if not verify_type(v, val_type) and not verify_generic_type(v,
                                                                        val_type):
                raise TypeError(
                    f"Hodnota pro klíč {k} neodpovídá typu {val_type}")
        except TypeError as e:
            raise TypeError(f"Chyba v hodnotě slovníku pro klíč {k}: {str(e)}")


def _verify_set_elements(value, args):
    """Ověří prvky množiny."""
    # Pro prázdnou množinu není co ověřovat
    if not value:
        return

    # Typ prvků množiny
    elem_type = args[0]

    # Ověření každého prvku (u množiny nemáme indexy)
    for item in value:
        try:
            # Rekurzivní ověření
            if not verify_type(item, elem_type) and not verify_generic_type(
                    item, elem_type):
                raise TypeError(f"Prvek {item} neodpovídá typu {elem_type}")
        except TypeError as e:
            # Přidáme kontext
            raise TypeError(f"Chyba v prvku množiny {item}: {str(e)}")


def _verify_tuple_elements(value, args):
    """Ověří prvky n-tice."""
    # Kontrola délky n-tice
    if len(value) != len(args) and args[-1] is not Ellipsis:
        raise TypeError(f"Očekáváno {len(args)} prvků, obdrženo {len(value)}")

    # Proměnná délka n-tice (Tuple[int, ...])
    if args and args[-1] is Ellipsis:
        elem_type = args[0]
        for i, item in enumerate(value):
            try:
                if not verify_type(item, elem_type) and not verify_generic_type(
                        item, elem_type):
                    raise TypeError(
                        f"Prvek na indexu {i} neodpovídá typu {elem_type}")
            except TypeError as e:
                raise TypeError(f"Chyba v n-tici na indexu {i}: {str(e)}")
    # Pevná délka n-tice (Tuple[int, str, bool])
    else:
        for i, (item, type_) in enumerate(zip(value, args)):
            try:
                if not verify_type(item, type_) and not verify_generic_type(
                        item, type_):
                    raise TypeError(
                        f"Prvek na indexu {i} neodpovídá typu {type_}")
            except TypeError as e:
                raise TypeError(f"Chyba v n-tici na indexu {i}: {str(e)}")


def _verify_union_type(value, args):
    """Ověří typ Union."""
    # Zkusíme všechny typy v Union
    errors = []
    for type_ in args:
        try:
            # Pokud kterýkoliv typ odpovídá, je to v pořádku
            if verify_type(value, type_) or verify_generic_type(value, type_):
                return
        except TypeError as e:
            errors.append(str(e))

    # Pokud žádný typ neodpovídá
    raise TypeError(
        f"Hodnota {value} neodpovídá žádnému z typů v Union: {', '.join(str(errors))}")


def _verify_optional_type(value, args):
    """Ověří typ Optional."""
    # None je vždy platný pro Optional
    if value is None:
        return

    # Jinak ověříme vnitřní typ
    type_ = args[0]
    if not verify_type(value, type_) and not verify_generic_type(value, type_):
        raise TypeError(f"Hodnota {value} neodpovídá typu {type_}")
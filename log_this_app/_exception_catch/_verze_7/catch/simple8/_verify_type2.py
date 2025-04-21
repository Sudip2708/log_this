from typing import get_origin, get_args, Union, List, Dict, Set, Tuple, Any, Optional,


def verify_dict_items(value):

    if isinstance(value, dict):

        pass


def verify_container_items(value):

    if isinstance(value, (list, set, tuple)):

        pass


def verify_generic_type(value, generic_type):
    """Ověří, zda hodnota odpovídá očekávanému generickému typu."""

    # Ověření, zda jde o generický typ
    if get_origin(generic_type) is not None:

        # Ověření kontejneru
        container_type = get_origin(generic_type)
        if not verify_type(value, container_type):
            raise TypeError( f"Očekáván typ kontejneru {container_type}, obdržen {type(value)}")

        # Ověření zda má definované i vnitřní hodnoty
        inner_types = get_args(generic_type)
        if inner_types:

            # Procházení argumentů
            for inner_type, inner_value in zip(inner_types, value):
                verify(inner_value, inner_type)

                if container_type in {list, tuple, set, frozenset, deque}:
                    verify_container_items(args)

                elif container_type in {dict, defaultdict, OrderedDict, ChainMap, Counter}:
                    verify_dict_items(args)

                elif container_type in {Union, Optional}:
                    verify_union_items(args)

                elif container_type in {NamedTuple, TypedDict, Protocol}:
                    verify_structured_type(args)

                elif container_type is Literal:
                    verify_literal(value, args)

                elif container_type is Type:
                    verify_class_type(value, args)

                elif container_type is Final:
                    return True  # Final se neověřuje

                elif container_type is Concatenate:
                    return True  # Concatenate se používá jen u Callable

                else:
                    raise TypeError( f"Nebyl zadán podporovaný objekt knihovny Typing: {container_type}.")

        # Pokud všechno ověření proběhne v pořádku
        return True

    # Pokud se nejedná o generický zápis
    return False







def verify(value, expected_type):
    """Ověří, zda hodnota odpovídá očekávanému typu, včetně generických typů."""

    # Ověří typu (je-li expected_type předáno jako typ)
    if verify_type(value, expected_type):
        return True

    # Ověří generického typu (je-li expected_type předáno jako generický typ)
    if verify_generic_type(value, expected_type):
        return True

    # Pokud ani jeedno ověření není pravdivé (nejedná se o typ ani generický typ)
    raise TypeError(f"Neplatný typ pro ověření: {expected_type}")


def verify_type(value, expected_type):
    """Ověří, zda hodnota odpovídá očekávanému typu."""

    # Přímé ověření typu (pokud expected_type je předán jako typ str, int, ...)
    if isinstance(expected_type, type):

        # Ověření pravdivosti
        if isinstance(value, expected_type):
            return True

        # Vyvolání výjimky pokud se ověření nepvedlo
        raise TypeError(
            f"Očekáván typ {expected_type}, obdržen {type(value)}")

    # Pokud expected_type není obyčejným typem
    return False

def verify_generic_type(value, generic_type):
    """Ověří, zda hodnota odpovídá očekávanému generickému typu."""

    # Ověření, zda jde o generický typ
    if get_origin(generic_type) is not None:

        # Ověření kontejneru
        container_type = get_origin(generic_type)
        if not verify_type(value, container_type):
            raise TypeError(
                f"Očekáván typ kontejneru {container_type}, obdržen {type(value)}")

        # Ověření zda má definované i vnitřní hodnoty
        inner_types = get_args(generic_type)
        if inner_types:

            # Procházení argumentů
            for inner_type, inner_value in zip(inner_types, value):
                verify(inner_value, inner_type)

        # Pokud všechno ověření proběhne v pořádku
        return True

    # Pokud se nejedná o generický zápis
    return False




    origin = get_origin(expected_type)  # Vrátí základní kontejnerový typ, např. list pro List[int]
    args = get_args(expected_type)  # Vrátí typy uvnitř, např. (int,) pro List[int]

    if origin and args:  # Pokud má origin a má definované vnitřní typy
        if not isinstance(value, origin):
            raise TypeError(f"Očekáván typ {origin}, obdržen {type(value)}")

        # 3. Ověření vnitřního obsahu pomocí pomocné funkce
        _verify_inner_contents(value, args)
        return True

    # 4. Pokud selže i tato kontrola, vyvoláme výjimku
    raise TypeError(f"Očekáván typ {expected_type}, obdržen {type(value)}")


def _get_container_and_arguments(expected_type):
    # Načtení typu kontejneru, např. list pro List[int]
    origin = get_origin(expected_type)
    # Načtení obsahu kontejneru
    args = get_args(expected_type)
    return origin, args

def _verify_generic_type(expected_type):
    """Pomocná funkce pro ověření obsahu generických typů."""

    # Načtení typu kontejneru, např. list pro List[int]
    origin = get_origin(expected_type)

    # Načtení obsahu kontejneru
    args = get_args(expected_type)
    


def _verify_inner_contents(container, expected_inner_types):
    """Pomocná funkce pro ověření obsahu generických typů."""

    if isinstance(container, (list, set, tuple)):  # Pro List, Set, Tuple
        inner_type = expected_inner_types[
            0]  # Většinou jeden typ, např. List[int] -> int

        for item in container:
            if not isinstance(item, inner_type):
                raise TypeError(
                    f"Očekáván prvek typu {inner_type}, obdržen {type(item)}")

    elif isinstance(container, dict):  # Pro Dictionary
        key_type, value_type = expected_inner_types  # Dict[int, str] -> (int, str)

        for key, value in container.items():
            if not isinstance(key, key_type):
                raise TypeError(
                    f"Očekáván klíč typu {key_type}, obdržen {type(key)}")
            if not isinstance(value, value_type):
                raise TypeError(
                    f"Očekávána hodnota typu {value_type}, obdržena {type(value)}")

from typing import Any, Tuple, Union

_MISSING = object()

def get_attr_safe(obj: Any, names: Union[str, Tuple[str, ...]], default: Any = _MISSING) -> Union[Any, Tuple[Any, ...]]:
    """
    Bezpečně získá jeden nebo více atributů z objektu.

    Args:
        obj: Objekt, ze kterého se mají získat atributy.
        names: Jméno jednoho atributu (str) nebo tuple jmen atributů.
        default: Volitelná výchozí hodnota, která se vrátí, pokud atribut neexistuje
                 a 'names' je jeden řetězec. Pokud 'names' je tuple a některý
                 atribut chybí, je vyvolána AttributeError.

    Returns:
        Hodnota jednoho atributu nebo tuple hodnot atributů.
        Pokud 'names' je jeden řetězec a atribut neexistuje a je zadána 'default',
        vrací se 'default'.
        Pokud 'names' je tuple a některý atribut neexistuje, je vyvolána AttributeError.
    """
    if isinstance(names, str):
        try:
            if default is _MISSING:
                return getattr(obj, names)
            else:
                return getattr(obj, names, default)
        except AttributeError as e:
            print(f"Objekt nemá atribut '{names}': {e}")
            if default is _MISSING:
                raise  # Pokud není default, vyvolej původní chybu
            return default
        except Exception as e:
            print(f"Došlo k chybě při získávání atributu '{names}': {e}")
            raise
    elif isinstance(names, tuple):
        results = []
        for name in names:
            try:
                results.append(getattr(obj, name))
            except AttributeError as e:
                print(f"Objekt nemá atribut '{name}': {e}")
                raise  # Pro tuple atributů vždy vyvolej AttributeError, pokud chybí
            except Exception as e:
                print(f"Došlo k chybě při získávání atributu '{name}': {e}")
                raise
        return tuple(results)
    else:
        raise TypeError("Argument 'names' musí být typu str nebo tuple.")
from typing import Any, Tuple, Union

from ..._exceptions import (
    GetSelfClassTypeError,
    GetSelfClassKeyError,
    GetSelfClassAttributeError,
    InternalUnexpectedError
)

def get_self_class(
        expected: Union[type, Tuple[type, ...]],
        custom_types: dict = None,
):
    """Pomocná funkce pro získání třídy objektu z custom contextu pro ověřování typu Self.

    Tato funkce slouží jako vnitřní validátor při zpracování typové anotace `Self`,
    která vyžaduje znalost instance `self` v době validace. Pro úspěšné ověření musí být
    do parametru `custom_types` předán kontext s klíčem `expected`, který bude
    reprezentovat právě `self` a jeho hodnotou bude samotná instance.

    Například při ověřování typu `Self` u nějaké metody je potřeba zajistit, že do
    `custom_types` bude přidán záznam typu `{"Self": self}`.

    Args:
        expected (str): Očekávaný název klíče (`např. "Self"`) v kontextovém slovníku.
        custom_types (dict): Kontextový slovník, kde `expected` slouží jako klíč
            a odpovídající hodnota obsahuje instanci, z níž bude získána třída.

    Returns:
        type: Třída (typ) objektu odpovídajícího zadanému klíči.

    Raises:
        GetSelfClassTypeError: Pokud `custom_types` není indexovatelný.
        GetSelfClassKeyError: Pokud `expected` není klíčem v `custom_types`.
        GetSelfClassAttributeError: Pokud objekt nemá atribut `__class__`.
        InternalUnexpectedError: Pokud nastane jiná neočekávaná výjimka.
    """
    try:
        # Načtení a navrácení třídy
        return custom_types[expected].__class__

    # Zachycení pokud custom_types není dict, ale třeba None nebo objekt bez podpory indexace
    except TypeError as e:
        raise GetSelfClassTypeError(expected, custom_types) from e

    # Zachycení pokud expected není klíč v custom_types
    except KeyError as e:
        raise GetSelfClassKeyError(expected, custom_types) from e

    # Zachycení pokud custom_types[expected] nevrátí objekt s atributem __class__
    except AttributeError as e:
        raise GetSelfClassAttributeError(expected, custom_types) from e

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise InternalUnexpectedError(e) from e



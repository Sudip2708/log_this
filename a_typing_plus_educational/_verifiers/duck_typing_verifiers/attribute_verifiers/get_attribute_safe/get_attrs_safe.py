from typing import Any, Dict, Iterable, List

from ..._exceptions_base import VerifyUnexpectedInternalError
from ..._tools import is_iterable_container
from .._exceptions import (
    VerifyAttributeNotFoundError,
    VerifyAttributeNotStrError,
    VerifyAttributeAccessError,
    VerifyAttributesNotIterableError,
    VerifyAttributesNotFoundError,
)
from .get_attr_safe import get_attr_safe

_MISSING = object()  # Sentinel pro detekci nezadaného defaultu


def get_attrs_safe(
        obj: Any,
        attribute_names: Iterable[str],
        default: Any = _MISSING,
        strict: bool = True
)-> List[Any] | Dict[str, Any]:

    # Kontrola zda jsou jména atributů předány jako iterovatelný objekt
    if not is_iterable_container(attribute_names):
        raise VerifyAttributesNotIterableError(attribute_names)

    # Výsledkový slovník
    outcome = {
        "attributes": [],
        "errors": {
            "not_str": [],
            "absent": [],
            "not_access": []
        }
    }

    try:

        # Procházení jmen atriubutů
        for attribute_name in attribute_names:

            try:

                # Pokus o získání atributů
                outcome["attributes"].append(
                    get_attr_safe(obj, attribute_name, default)
                )

            # Pokud jméno atributu není zadáno jako řetězec
            except VerifyAttributeNotStrError:
                outcome["errors"]["not_str"].append(attribute_name)

            # Pokud atribut nebyl nalezen
            except VerifyAttributeNotFoundError:
                outcome["errors"]["absent"].append(attribute_name)

            # Pokud se k atributu nepovedlo připojit
            except VerifyAttributeAccessError:
                outcome["errors"]["not_access"].append(attribute_name)

        # Pokud není striktní režim (navrácení výsledkového slovníku)
        if not strict:
            return outcome

        # Pokud je striktní režim a nepovedlo se najít všechny atributy (vyvolání výjimky)
        if (
                outcome["errors"]["not_str"]
                or outcome["errors"]["absent"]
                or outcome["errors"]["not_access"]
        ):
            raise VerifyAttributesNotFoundError(obj, attribute_names, outcome)

        # Pokud je striktní režim a vše proběhlo v pořádku (navrácení seznamu s atributy)
        return outcome["attributes"]

    # Propagace případné neočekávané výjimky z předešlého kodu
    except VerifyUnexpectedInternalError:
        raise

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e


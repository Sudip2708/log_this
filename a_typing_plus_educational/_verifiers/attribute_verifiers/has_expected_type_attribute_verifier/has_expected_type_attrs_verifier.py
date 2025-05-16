from typing import Any, Type
from collections.abc import Iterable

from ..._exceptions_base import (
    VerifyUnexpectedInternalError,
    VerifyError
)
from ..._tools import is_iterable_container
from .._exceptions import (
    VerifyAttributeNotStrError,
    VerifyAttributeAccessError,
    VerifyAttributeNotFoundError,
    VerifyAttributesNotIterableError,
    VerifyAttributesNotExpectedTypeError
)
from .has_expected_type_attr_verifier import (
    has_expected_type_attr_verifier,
    # VerifyTypeParameterError
)


def has_expected_type_attrs_verifier(
    obj: Any,
    attribute_names: Iterable[str],
    expected_type: Type,
    bool_only: bool = False
) -> bool:

    # Kontrola zda jsou jména atributů předány jako iterovatelný objekt
    if not is_iterable_container(attribute_names):
        raise VerifyAttributesNotIterableError(attribute_names)

    # Výsledkový slovník
    outcome = {
        "attributes": [],
        "errors": {
            "not_expected_type": [],
            "not_str": [],
            "absent": [],
            "not_access": []
        }
    }

    try:

        # Procházení jmen atriubutů
        for attribute_name in attribute_names:

            try:

                # Pokus o ověření atributu
                if has_expected_type_attr_verifier(
                        obj, attribute_name, expected_type, bool_only=True
                ):
                    outcome["attributes"].append(attribute_name)

                # Pokud ověření je negativní
                outcome["errors"]["not_expected_type"].append(attribute_name)

            # Pokud jméno atributu není zadáno jako řetězec
            except VerifyAttributeNotStrError:
                outcome["errors"]["not_str"].append(attribute_name)

            # Pokud atributu není nalezen
            except VerifyAttributeNotFoundError:
                outcome["errors"]["absent"].append(attribute_name)

            # Pokud se k atributu nepovedlo připojit
            except VerifyAttributeAccessError:
                outcome["errors"]["not_access"].append(attribute_name)

        # Pokud se nepovedlo najít všechny atributy (vyvolání výjimky)
        if (
                outcome["errors"]["not_int"]
                or outcome["errors"]["not_str"]
                or outcome["errors"]["absent"]
                or outcome["errors"]["not_access"]
        ):

            # Pokud je režim pouze bool, vrať False bez vyhazování výjimky
            if bool_only:
                return False

            # Jinak vyhoď výjimku pro nevalidní hodnotu
            raise VerifyAttributesNotExpectedTypeError(obj, attribute_names, outcome)

        # Pokud objekt obsahuje všechny atributy
        return True

    # Přeposlání všech vlastních výjimek
    # except (
    #     VerifyAttributesNotExpectedTypeError,  # Propagace vnitřní výjimky
    #     VerifyTypeParameterError,  # Propagace výjinky vyvolané při zadání nevalidního typu (zachytí is_instance_verifier)
    #     VerifyUnexpectedInternalError  # Propagace dříve zachycených neočekávaných výjimek
    # ):
    except VerifyError:
        raise

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e



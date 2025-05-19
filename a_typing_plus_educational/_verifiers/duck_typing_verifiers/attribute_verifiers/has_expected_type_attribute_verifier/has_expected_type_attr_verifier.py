from typing import Any, Type

from ..._exceptions_base import (
    VerifyUnexpectedInternalError,
    VerifyError
)
from ...value_verifiers import (
    is_instance_verifier,
    VerifyIsInstanceReturnedFalseError,  # Nepoužitá výjimka, importovaná pro init balíčku
    VerifyTypeParameterError  # Nepoužitá výjimka, importovaná pro init balíčku
)
from ..get_attribute_safe import (
    get_attr_safe,
    VerifyAttributeNotFoundError,  # Nepoužitá výjimka, importovaná pro init balíčku
    VerifyAttributeNotStrError,  # Nepoužitá výjimka, importovaná pro init balíčku
    VerifyAttributeAccessError,  # Nepoužitá výjimka, importovaná pro init balíčku
)


def has_expected_type_attr_verifier(
    obj: Any,
    attribute_name: str,
    expected_type: Type,
    bool_only: bool = False
) -> bool:

    try:

        # Získání atributu
        attribute = get_attr_safe(obj, attribute_name)

        # Kontrola zda je atribut volatelný
        return is_instance_verifier(attribute, expected_type, bool_only)

    # Přeposlání všech vlastních výjimek
    # except (
    #     VerifyAttributeNotStrError,  # Když parametr pro jméno atributu není zadán jako řetězec (zachytí get_attr_safe)
    #     VerifyAttributeNotFoundError,  # Když atribut na objektu není nalezený (zachytí get_attr_safe)
    #     VerifyAttributeAccessError,  # Když k atributu není přístup (zachytí get_attr_safe)
    #     VerifyIsInstanceReturnedFalseError,  # Když atribut není typu int - celočíselná hodnota (zachytí is_instance_verifier)
    #     VerifyTypeParameterError,  # Když když je požadovaný typ zadán nevalidním způsobem (zachytí is_instance_verifier)
    #     VerifyUnexpectedInternalError  # Propagace dříve zachycených neočekávaných výjimek
    # ):
    except VerifyError:
        raise

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e

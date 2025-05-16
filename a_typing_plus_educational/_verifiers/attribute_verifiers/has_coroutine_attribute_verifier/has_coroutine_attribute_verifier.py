from typing import Any, Iterable, Union
from collections.abc import Iterable as IterableOrigin

from .._exceptions import VerifyAttributeParameterError
from .has_coroutine_attr_verifier import has_coroutine_attr_verifier
from .has_coroutine_attrs_verifier import has_coroutine_attrs_verifier


def has_coroutine_attribute_verifier(
    obj: Any,
    attribute: Union[str, Iterable[str]],
    bool_only: bool = False
) -> bool:

    # Vyřízení pro jednu položku
    if isinstance(attribute, str):
        return has_coroutine_attr_verifier(obj, attribute, bool_only)

    # Vyřízení pro více položek
    if isinstance(attribute, IterableOrigin):
        return has_coroutine_attrs_verifier(obj, attribute, bool_only)

    # Výjimka pro nevalidní vstup
    raise VerifyAttributeParameterError(attribute)




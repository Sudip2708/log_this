from typing import Any, Iterable, Union
from collections.abc import Iterable as IterableOrigin

from .._exceptions import VerifyAttributeParameterError
from .get_attr_safe import get_attr_safe
from .get_attrs_safe import get_attrs_safe

_MISSING = object()  # Sentinel pro detekci nezadaného defaultu


def get_attribute_safe(
        obj: Any,
        attribute: Union[str, Iterable[str]],
        default: Any = _MISSING,
        strict: bool = True
) -> Any:

    # Vyřízení pro jednu položku
    if isinstance(attribute, str):
        return get_attr_safe(obj, attribute, default)

    # Vyřízení pro více položek
    if isinstance(attribute, IterableOrigin):
        return get_attrs_safe(obj, attribute, default, strict)

    # Výjimka pro nevalidní vstup
    raise VerifyAttributeParameterError(attribute)

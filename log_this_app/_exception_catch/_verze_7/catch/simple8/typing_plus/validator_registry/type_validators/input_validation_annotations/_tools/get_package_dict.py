from typing import Dict, Type
from .._base_type_validator import BaseTypeValidator

def get_package_dict(*validator_classes: Type[BaseTypeValidator]) -> Dict[str, Type[BaseTypeValidator]]:
    """
    Vytvoří slovník, kde klíčem je VALIDATOR_KEY a hodnotou je validační třída.

    Args:
        *validator_classes: Libovolný počet tříd, které dědí z BaseTypeValidator.

    Returns:
        Slovník ve formátu {VALIDATOR_KEY: třída}
    """
    result = {}
    for cls in validator_classes:
        if not issubclass(cls, BaseTypeValidator):
            raise TypeError(f"{cls.__name__} není potomek BaseTypeValidator.")
        key = getattr(cls, "VALIDATOR_KEY", None)
        if not key:
            raise AttributeError(f"{cls.__name__} nemá definovaný VALIDATOR_KEY.")
        result[key] = cls()
    return result

from typing import List, Type
from .._base_type_validator import BaseTypeValidator

def get_package_names(*validator_classes: Type[BaseTypeValidator]) -> List[str]:
    """
    Vytvoří seznam, kde kde všechny třídy jsou jako str.

    Args:
        *validator_classes: Libovolný počet tříd, které dědí z BaseTypeValidator.

    Returns:
        Slovník ve formátu {VALIDATOR_KEY: třída}
    """
    result = []
    for cls in validator_classes:
        if not issubclass(cls, BaseTypeValidator):
            raise TypeError(f"{cls.__name__} není potomek BaseTypeValidator.")
        result.append(cls.__name__)
    return result

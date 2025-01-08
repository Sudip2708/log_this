# log_this/manager/config/cli/handlers/_value_handler.py
from typing import Union


def parse_input_value(value: str) -> Union[int, str, bool, None]:
    """
    Převede string hodnotu z příkazové řádky na správný datový typ.

    Args:
        value (str): Hodnota z příkazové řádky

    Returns:
        Union[int, str, bool]: Převedená hodnota na správný datový typ
    """

    # Speciální hodnota pro docstring_lines
    if value.lower() == 'all':
        return 'all'

    # Převod pro boolean
    if value.lower() in ('true', 'false'):
        return value.lower() == 'true'

    # Převod pro integer
    try:
        return int(value)
    except ValueError:
        pass

    # Pokud hodnota nebyla spracovaná
    return None
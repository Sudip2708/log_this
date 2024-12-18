from typing import Any


def validate_value(value: Any, default_value: Any, key: Any) -> Any:
    """
    Validuje hodnotu pro daný klíč

    Args:
        value: Vstupní hodnota
        default_value: Defaultní hodnota pro případ neplatnosti
        key: Klíč pro danou hodnotu

    Returns:
        Validovaná hodnota
    """
    try:
        if key == 'max_depth' and isinstance(value, int):
            return value
        if key == 'blank_lines' and value in {True, False, 0, 1}:
            return value
        if key == 'docstring_lines' and (isinstance(value, int) or value == 'all'):
            return value
        if isinstance(default_value, int) and 0 <= value <= 4:
            return value
        return default_value
    except (TypeError, ValueError):
        return default_value
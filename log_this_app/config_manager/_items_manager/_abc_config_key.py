from abc import ABC
from typing import Any, Dict, Union, Tuple

CONFIG_CATEGORY = {
    "log_this_modes": "Nastavení módu logeru",
    "log_this_aspects": "Nastavení vzhledu logeru",
    "interactive_cli": "Nastavení vzhledu interaktivního menu",
}

class ConfigKey(ABC):
    """Abstraktní základní třída pro konfigurační klíče"""

    # Třídní atributy které musí být definovány v potomcích
    INFO: str
    DEFAULT_VALUE: Union[int, str, bool]
    LABEL: str
    OPTIONS: Tuple[str, ...]
    HINT: Tuple[str, ...]
    VALUES_DICT: Dict[Union[int, str, bool], str]
    CATEGORY: str  # Bude validováno

    REQUIRED_ATTRIBUTES = {
        "INFO": (str, type(None)),  # None je zde kuli mezitřídě ModeConfigKey
        "DEFAULT_VALUE": (int, str, bool, type(None)),  # None je zde kuli mezitřídě ModeConfigKey
        "LABEL": (str, type(None)),  # None je zde kuli mezitřídě ModeConfigKey
        "OPTIONS": tuple,
        "HINT": tuple,
        "VALUES_DICT": dict,
        "CATEGORY": str,
    }

    def validate(self, value: Any) -> bool:
        """Výchozí validace: kontrola, zda je hodnota v `VALUES_DICT`."""
        return value in self.VALUES_DICT

    def __init_subclass__(cls, **kwargs):
        """Automaticky ověřuje, že podtřídy mají všechny povinné atributy a správné typy."""
        super().__init_subclass__(**kwargs)

        # Kontrola přítomnosti všech atributů
        for attr, expected_type in cls.REQUIRED_ATTRIBUTES.items():
            if not hasattr(cls, attr):
                raise TypeError(f"Třída {cls.__name__} musí definovat atribut '{attr}'.")

            # Typová kontrola obsahu atributů
            value = getattr(cls, attr)
            if not isinstance(value, expected_type):
                raise TypeError(
                    f"Atribut '{attr}' v třídě {cls.__name__} musí být typu {expected_type}, ale je {type(value)}!"
                )

        # Kontrola, zda je CATEGORY validní
        if cls.CATEGORY not in CONFIG_CATEGORY:
            raise ValueError(
                f"Třída {cls.__name__} má neplatnou CATEGORY '{cls.CATEGORY}'. "
                f"Povolené hodnoty: {list(CONFIG_CATEGORY.keys())}"
            )


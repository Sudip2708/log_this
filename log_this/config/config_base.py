from typing import Dict, Union
from .mixins_data import ConfigMixin



class LogThisConfig(ConfigMixin):
    """
    Singleton konfigurace pro knihovnu logování s rozšířenými funkcemi.

    Hlavní vlastnosti:
    - Jedinečná instance konfigurace v aplikaci
    - Automatické načítání a validace konfigurace z JSON souboru
    - Dynamická správa konfiguračních parametrů
    - Podpora exportu, importu a resetu konfigurace
    """

    # Atribut pro instanci třídy:
    _instance = None

    # Defaultní hodnoty:
    DEFAULTS: Dict[str, Union[int, str, bool]] = {
        'skip_this': 0,
        'one_line': 1,
        'simple': 2,
        'detailed': 3,
        'report': 4,
        'true': 1,
        'false': 0,
        'none': 0,
        'empty': 0,
        'indent': 2,
        'blank_lines': True,
        'docstring_lines': 3,
        'max_depth': 100,
    }

    # Vytvoření instance:
    def __new__(cls) -> 'LogThisConfig':
        """
        Implementace singleton vzoru.

        Vytvoří jedinou instanci konfigurace nebo vrátí existující.

        Returns:
            LogThisConfig: Singleton instance konfigurace
        """
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.config = cls._load_default_config()
        return cls._instance

    # Výpis aktuálního nastavení:
    def __str__(self) -> str:
        """
        Vrací čitelnou reprezentaci konfigurace ve formě řetězce.

        Returns:
            str: Formátovaný výpis aktuální konfigurace.
        """
        formatted_config = "\n".join(
            f"{key}: {value}" for key, value in self.config.items())
        return f"LogThisConfig:\n{formatted_config}"


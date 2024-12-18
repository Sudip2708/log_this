import os
from random import choice

from ._loader_mixin import ConfigLoaderMixin


class LogThisConfig(ConfigLoaderMixin):
    """
    Singleton třída pro správu konfigurace.

    Hlavní vlastnosti:
    - Zajišťuje jedinečnou instanci konfigurace v celé aplikaci
    - Uchovává globální konfigurační nastavení
    - Automaticky načítá a validuje konfiguraci z JSON souboru
    """

    # Singleton instance - bude uchovávat jedinou instanci třídy
    _instance = None

    # Výchozí mapování hodnot pro různé typy klíčů
    values = {
        'skip_this': 0,  # Přeskočení logování
        'one_line': 1,  # Nastavení pro jeden řádek
        'simple': 2,  # Základní nastavení
        'detailed': 3,  # Detailní nastavení
        'report': 4,  # Nastavení pro reporting
        True: 1,  # Mapování boolean True
        False: 0,  # Mapování boolean False
        None: 0,  # Mapování None
        '': 0,  # Mapování prázdného řetězce
    }

    # Výchozí nastavení odsazení a prázdných řádků
    indent = 2  # Počet znaků pro odsazení od kraje při zanoření
    blank_lines = True  # Zobrazení prázdného řádku mezi jednotlivými logy
    docstring_lines = 3  # Počet řádků z docstringu pro report
    max_depth = 100  # Úroveň maximálního zanoření


    def __new__(cls):
        """
        Implementace singleton vzoru.

        Pokud instance neexistuje, vytvoří ji a načte konfiguraci.
        Při opakovaném volání vrací stávající instanci.

        Returns:
            LTConfig: Jediná instance třídy
        """

        # Kontrola, zda již existuje vytvořená singleton instance
        if not cls._instance:

            # Načtení cesty k adresáři tohoto souboru
            config_dir = os.path.dirname(__file__)

            # Vytvoření cesty ke konfiguračnímu slovníku
            config_path = os.path.join(config_dir, 'config.json')

            # Vytvoření nové instance
            cls._instance = super().__new__(cls)

            # Načtení konfigurace
            cls._load_config(config_path)

        return cls._instance

    def get_attributes_dict(self):
        """Vrátí hodnoty instance jako slovník"""
        return {

            'skip_this': self.values.get('skip_this') # Textová reprezentce pro mod 0
            'one_line': self.values.get('one_line'),  # Textová reprezentce pro mod 1
            'simple': self.values.get('simple'),  # Textová reprezentce pro mod 2
            'detailed': self.values.get('detailed'),  # Textová reprezentce pro mod 3
            'report': self.values.get('report'),  # Textová reprezentce pro mod 4

            'true': self.values.get(True),   # Další možnost zápisu pro mod 1
            'false': self.values.get(False),   # Další možnost zápisu pro mod 0
            'none': self.values.get(None),   # Další možnost zápisu pro mod 0
            'empty': self.values.get(''),   # Prázdné závorky jako prostředek pro jakoukoliv hodnotu (defaultně 0)

            'indent': self.indent,  # Počet znaků pro odsazení od kraje při zanoření (0-4)
            'blank_lines': self.blank_lines,  # Zobrazení prázdného řádku mezi jednotlivými logy (True/False)
            'docstring_lines': self.docstring_lines,  # Počet řádků z docstringu pro report (int a nebo 'all' pro všechny)
            'max_depth': self.max_depth  # Úroveň maximálního zanoření pro detekci cyklického vstupu

        }

    def set_value(self, key, value, choices=(0, 1, 2, 3, 4)):
        """Metoda na aktualizaci hodnot"""
        error = ValueError(f"Hodnota {value}, "
                           f"není platnou hodnotu pro {key}. "
                           f"Platné hodnoty: {choices}")

        if key in ('skip_this', 'one_line', 'simple', 'detailed', 'report'):
            if value in choices:
                self.values[key] = value
            else:
                raise error

        if key in ('true', 'false', 'none', 'empty'):
            if value in choices:
                if key == 'true':
                    self.values[True] = value
                elif key == 'false':
                    self.values[False] = value
                elif key == 'none':
                    self.values[None] = value
                elif key == 'empty':
                    self.values[''] = value
            else:
                raise error

        if key in ('indent', 'blank_lines', 'docstring_lines', 'max_depth')
            if key == 'indent':
                if value in choices:
                    self.indent = value
                else:
                    raise error
            elif key == 'blank_lines':
                choices = (0, 1, True, False)
                if value in choices:
                    self.blank_lines = value
                else:
                    raise error
            elif key == 'docstring_lines':
                if isinstance(value, int) or value == 'all':
                    self.docstring_lines = value
                else:
                    choices = (int, 'all')
                    raise error
            elif key == 'max_depth':
                if isinstance(value, int):
                    self.max_depth = value
                else:
                    choices = (int,)
                    raise error





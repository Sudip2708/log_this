"""
Závisosti:
- _read_existing_config: Metoda pro načtení konfigurace z konfiguračního souboru
- defaults: Atribut obsahující slovník s klíči a defaultními hodnotami
- _create_config_file: Boolena atribut pro nastavení oprávnění k vytvoření nového konfiguračního souboru (bez tohoto atributu s hodnotu True vytvoření nového souboru neprojde)
"""

from abc import ABC, abstractmethod
from typing import Dict, Union, Optional, Any, Set
import logging
from pathlib import Path

from ._read_existing_config import ReadExistingConfigMixin
from ._load_and_validate_config import LoadAndValidateConfigMixin
from ._validate_key_and_value import ValidateKeyAndValueMixin
from ._merge_with_defaults import MargeWithDefaultsMixin

class LoadConfigMixin(
    ABC,
    ReadExistingConfigMixin,
    LoadAndValidateConfigMixin,
    ValidateKeyAndValueMixin,
    MargeWithDefaultsMixin,
):
    """
    Centrální mixin pro třídu LogThisConfig, spojující veškeré metody potřebné pro inicializaci konfigurace.

    Obsahuje všechny metody a atributy nezbytné pro správnou funkčnost a musí být implementován
    ve třídě, která ho rozšiřuje.

    Abstraktní vlastnosti očekávané v inicializační třídě:
        - `keys_data`: Slovník s daty o klíčích konfigurace.
        - `cli_log`: Logger pro komunikaci skrze CLI.
        - `_config_path`: Cesta ke konfiguračnímu souboru.
        - `_create_config_file`: Boolean, povolující vytvoření konfiguračního souboru.
        - `config`: Slovník s aktuální konfigurací.
        - `defaults`: Výchozí hodnoty konfigurace.
        - `valid_keys`: Množina platných klíčů.

    Abstraktní metody které přidává tento mixin:
        - `load_config`: Metoda pro načtení konfigurace (Hlavní metoda definovaná tímto mixinem).
        - `_read_existing_config`: Metoda pro načtení existující konfigurace.
        - `_load_and_validate_config`: Metoda pro načtení a validaci konfigurace.
        - `_validate_key_and_value`: Metoda pro validaci klíče a hodnoty.
        - `_merge_with_defaults`: Metoda pro sloučení konfigurace s výchozími hodnotami.
    """

    # Očekávané vlastnosti hlavní třídy
    @property
    @abstractmethod
    def _config_path(self) -> Path:
        pass

    @property
    @abstractmethod
    def _create_config_file(self) -> bool:
        """Boolean atribut povolující vytvoření nového konfiguračního souboru."""
        pass

    @_create_config_file.setter
    def _create_config_file(self, value: bool) -> None:
        self._create_config_file_value = value

    @property
    @abstractmethod
    def config(self) -> Dict[str, Union[int, str, bool]]:
        pass

    @property
    @abstractmethod
    def defaults(self) -> Dict[str, Union[int, str, bool]]:
        """Výchozí hodnoty konfigurace."""
        pass

    @property
    @abstractmethod
    def valid_keys(self) -> Set[str]:
        pass

    # Očekávané metody z mixinů
    @abstractmethod
    def _read_existing_config(self) -> Optional[
        Dict[str, Union[int, str, bool]]]:
        """Načte existující konfiguraci ze souboru."""
        pass



    def load_config(
            self
    ) -> Dict[str, Union[int, str, bool]]:
        """
        Načte konfiguraci ze souboru nebo vytvoří výchozí.

        Tato metoda má čistě za úkol vytvořit a předat konfigurační slovník,
        neřeší tedy zpracování výjimek při pokusu o načtení dat z existujícího souboru.
        Tuto logiku má na strosti metoda _read_existing_config,
        která vyjíimky nejen zachytává, ale i z nich vytváří výstupní log.

        Returns:
            Dict: Načtená nebo výchozí konfigurace
        """

        # Načtení konfigurace z konfiguračního souboru (pokud existuje)
        config_dict = self._read_existing_config()

        # Pokud se načtení nezdařilo, nebo konfigurační soubor neexistuje
        if not config_dict:

            # Načtení defaultní konfigurace a pokus o vytvoření konfiguračního souboru
            config_dict = self.defaults.copy()

            # Nastavení atribut deklarujícího vytvoření nového souboru
            self._create_config_file = True

        # Navrácebí slovníku s konfigurací
        return config_dict

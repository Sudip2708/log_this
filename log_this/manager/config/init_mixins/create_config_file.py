"""
Závislosti:
- _config_path: Atribut definující cestu ke konfiguračnímu souboru
- save_config_file: Funkce pro uložení konfiguračního souboru
- _create_config_file: Boolena atribut pro nastavení oprávnění k vytvoření nového konfiguračního souboru (bez tohoto atributu s hodnotu True vytvoření nového souboru neprojde)
- delete_config_file: Funkce pro smazání konfiguračního souboru

Zachytávání výjimek:
- SaveConfigError: Výjimky vyvolané při ukládání konfiguračního souboru
- DeleteConfigError: Výjimky vyvolané při smazání konfiguračního souboru
- ConfirmDeleteError: Výjimka vyvolaná pokud došlo ke snaze smazat konfigurační soubor bez předchozího nastavení hodnoty atributu _recreate_config_file na True
"""

from abc import ABC, abstractmethod
from typing import Dict, Union
from pathlib import Path
import logging

from ..utils import (
    save_config_file,
    delete_config_file,
)

from ..errors import (
    ConfirmDeleteError,
    DeleteConfigFileError,
    SaveConfigFileError
)



class CreateConfigFileMixin(ABC):
    """Mixin metody pro vytvoření konfiguračního souboru"""

    @property
    @abstractmethod
    def _config_path(self) -> Path:
        """Atribut s cestou ke konfiguračnímu souboru."""
        pass

    @property
    @abstractmethod
    def config(self) -> Dict[str, Union[int, str, bool]]:
        """Atribut slovníku s aktuální konfigurací."""
        pass

    @property
    @abstractmethod
    def _create_config_file(self) -> bool:
        """Boolean atribut povolující vytvoření nového konfiguračního souboru."""
        pass

    @property
    @abstractmethod
    def cli_log(self) -> logging.Logger:
        """Atribut pro logger pro komunikaci skrze CLI."""
        pass

    def create_config_file(self) -> None:
        """
        Vytvoří novou konfiguraci z výchozích hodnot.

        Returns:
            Dict: Nová konfigurace
        """

        try:

            # Kontrola, zda konfigurační soubor  neexistuje
            if not self._config_path.exists():

                # Volání metody pro vytvoření nového souboru
                save_config_file(self._config_path, self.config)

            # Pokud konfigurační soubor exsituje, kontrola zda je nastaven atribut povolující jeho smazání
            elif self._create_config_file:

                    # Volání funkce pro smazání souboru
                    delete_config_file(self._config_path)

                    # Volání metody pro vytvoření nového souboru
                    save_config_file(self._config_path, self.config)

            # Pokud není nastaven atribut pro jeho smazání na hodnotu True, bude vyvolaná výjimka
            else:
                raise ConfirmDeleteError(
                    "Pro smazání konfiguračního souboru je vyžadováno nastavení "
                    "self._recreate_config_file na True."
                )

        # Zachycení a spracování výjimek
        except (
                SaveConfigFileError,
                DeleteConfigFileError,
                ConfirmDeleteError
        ) as e:

            self.cli_log.warning(f"{e}", extra=e.extra)
            self.cli_log.info(
                "Konfigurační soubor pro trvalé uložení konfigurace není správně inicializován.",
                extra = {
                    "detail": "Tento nedostatek neovlivní funkčnost knihovny, pouze není možné změněné hodnoty uchovat do externího souboru.",
                    "hint": "Důvod proč nebylo možné vytvořit nový konfigurační soubor je uveden v předešlém logu. "
                }
            )
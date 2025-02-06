from abc import ABC, abstractmethod
from typing import Dict, Union
from pathlib import Path

from .access_tester import system_access_tester
from .cli.styler import cli_print
from .keys import KEYS_DATA
from .utils import load_and_validate_config_file, merge_with_defaults



class ImportConfigFromFileMixin(ABC):

    @abstractmethod
    @property
    def config(self) -> Dict[str, Union[int, str, bool]]:
        """Atribut se slovníkem s aktuálními hodnotami"""
        pass

    @abstractmethod
    @config.setter
    def config(self, config_dict: Dict[str, Union[int, str, bool]]) -> None:
        """Atribut se slovníkem s aktuálními hodnotami"""
        pass

    @abstractmethod
    def save_to_config_file(self):
        """Metoda pro uložení aktuální konfigurace do konfiguračního souboru (je-li používán)"""
        pass

    def import_config_from_file(
            self,
            file_path: Union[Path, str]
    ):

        # Převod na cesty na Path
        if not isinstance(file_path, Path):
            file_path = Path(file_path)

        # Ověření zda soubor na uvedeném umístění existuje
        if not file_path.exists():
            cli_print(
                style="error",
                info="Na uvedené cestě nebyl nalezen žádný soubor",
                detail=f"Uvedená cesta k souboru: {file_path}",
                hint="Zkontrolujte správnost cesty."
            )

        # Načtení a validace obsahu souboru
        file_config = load_and_validate_config_file(file_path)

        # Kontrola zda konfigurační soubor obsahuje všechny klíče
        if set(file_config.keys()) != set(KEYS_DATA.keys()):
            # Doplnění chybějícíh klíčů
            file_config = merge_with_defaults(file_config)

        # Kontrola, zda není již konfigurace načtena
        if self.config == file_config:
            cli_print(
                style="info",
                info="Konfigurace již obsahuje nastavení uvedené v souboru.",
                detail="Žádná změna nebyla učiněna,"
            )
            return

        # Uložení aktuální konfigurace
        self.config = file_config
        cli_print(
            style="success",
            info=f"Úspěšné přepsání celé konfigurace na defaultní hodnoty"
        )

        # Uložení změn do konfiguračního souboru (je-li používán)
        self.save_to_config_file()

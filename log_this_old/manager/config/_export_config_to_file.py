from abc import ABC, abstractmethod
from typing import Dict, Union
from pathlib import Path

from .access_tester import system_access_tester
from .cli.styler import cli_print
from .utils import save_config_file

class ExportConfigToFileMixin(ABC):

    @abstractmethod
    @property
    def config(self) -> dict:
        """Atribut se slovníkem s aktuálními hodnotami"""
        pass

    def export_config_to_file(
            self,
            file_path: Union[Path, str]
    ):

        # Převod na cesty na Path
        if not isinstance(file_path, Path):
            file_path = Path(file_path)

        # Ověření zda je možné soubor vytvořit
        system_access_tester(file_path)

        # Vytvoření souboru
        save_config_file(file_path, self.config)

        # Ověření existence souboru a výpis oznamu
        if file_path.exists():
            cli_print(
                style="success",
                info="Byl úspěšně vytvořen soubor s aktuální konfigurací.",
                detail=f"Soubor nalezneta na umístění: {file_path}"
            )
from abc import ABC, abstractmethod
from pathlib import Path

from .utils import delete_config_file, save_config_file
from .errors import DeleteConfigFileError, SaveConfigFileError
from .zzz import print_exceptions_warning


class SaveToConfigFileMixin(ABC):
    """Mixin třída pro správu konfiguračního souboru."""

    @abstractmethod
    @property
    def config_file(self) -> bool:
        """Atribut signalizující používání konfiguračního souboru"""
        pass

    @abstractmethod
    @config_file.setter
    def config_file(self, value: bool) -> None:
        """Setter pro atribut config_file"""
        pass

    @abstractmethod
    @property
    def config_file_path(self) -> Path:
        """Atribut vracející cestu ke konfiguračnímu souboru"""
        pass

    @abstractmethod
    @property
    def config(self) -> dict:
        """Atribut se slovníkem s aktuálními hodnotami"""
        pass


    def save_to_config_file(self) -> None:
        """Přepíše konfigurační soubor aktuální konfigurací."""

        # Kontrola zda se má používat ukládání do souboru
        if not self.config_file:
            return

        try:

            # Smazání původního souboru
            delete_config_file(self.config_file_path)

            # Vytvoření nového souboru
            save_config_file(self.config_file_path, self.config)


        except (
                DeleteConfigFileError,
                SaveConfigFileError
        ) as e:

            # Nastavení na nepoužívání souboru
            self.config_file = False

            # Oznam o nezdaru a nepoužívání konfiguračního souboru
            print_exceptions_warning(
                exception=e,
                conclusion=(
                    "Knihovna poběží i bez konfiguračního souboru."
                    "Jediné omezení je že případné změny konfigurace se vám neuloží do příště."
                )
            )


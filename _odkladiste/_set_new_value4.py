from abc import ABC, abstractmethod
from typing import Union, Set, Dict
from pathlib import Path

from .cli.styler import cli_print
from .validations import validate_key, validate_value
from .utils import delete_config_file, save_config_file
from .errors import (
    ValidateKeyError,
    ValidateValueError,
    ValueIsAlreadySetError,
    DeleteConfigFileError,
    SaveConfigFileError
)

from .cli.interactive.runners import run_config_settings


class SetNewValueMixin(ABC):

    @abstractmethod
    @property
    def config(self) -> dict:
        """Atribut se slovníkem s aktuálními hodnotami"""
        pass

    @abstractmethod
    @property
    def config_file(self) -> bool:
        """Atribut signalizující používání konfiguračního souboru"""
        pass

    @abstractmethod
    @config_file.setter
    def config_file(self, value: bool):
        """Setter pro atribut config_file"""
        pass

    @abstractmethod
    @property
    def config_file_path(self) -> Path:
        """Atribut vracející cestu ke konfiguračnímu souboru"""
        pass

    def set_new_value(
            self,
            key: str,
            value: Union[int, str, bool],
            value_check: bool = False
    ) -> None:

        raised_exception = False
        conclusion = ""
        e = None

        try:

            # Kontrola zda ještě není provedena validace
            if not value_check:
                validate_key(key)
                validate_value(key, value)

            # Kontrola, zda nebyla zadaná již existující hodnota
            if value == self.config[key]:
                raise ValueIsAlreadySetError(key, value)

            # Uložení změny do konfiguračního slovníku
            self.config[key] = value
            cli_print(
                style="success",
                info=f"Úspěšné nastavení klíče '{key}' na hodnotu: {value}"
            )

            # Uložení změn do konfiguračního souboru (je-li používán)
            if self.config_file:
                delete_config_file(self.config_file_path)
                save_config_file(self.config_file_path, self.config)


        # Zacycení zadání vadného klíče
        except ValidateKeyError as e:
            print_key_exceptions_warning(e)
            run_config_settings()  # Přepnutí na interaktivní režim pro zadání klíče

        # Zachycení zadání vadné hodnoty (předpokládá že klíč je správně)
        except ValidateValueError as e:
            print_value_exceptions_warning(e)
            run_config_settings(key)  # Přepnutí na interaktivní režim pro zadání klíče

        # Zachycení zadání již nastavené hodnoty
        except ValueIsAlreadySetError as e:
            print_value_is_already_set_warning(e)

        # Zachycení výjimky při smazání nebu ukládání konfiguračního souboru
        except (DeleteConfigFileError, SaveConfigFileError) as e:
            self.config_file = False  # Nastavení nepoužívání konfiguračního souboru
            print_file_exceptions_warning(e)


def print_exceptions_warning(exception, conclusion):
    """Funkce pro cli výpis chyby"""

    e = exception
    cli_print(
        style="warning",
        info=str(e),
        detail=e.detail,
        hint=e.hint,
        conclusion=conclusion
    )

def print_file_exceptions_warning(exception):
    """Funkce pro cli výpis chyby souboru"""
    print_exceptions_warning(exception, (
            "Knihovna poběží i bez konfiguračního souboru."
            "Jediné omezení je že případné změny konfigurace se vám neuloží do příště."
        )
    )

def print_value_is_already_set_warning(exception):
    """Funkce pro cli výpis že byla zadaná již nastavená hodnota"""
    print_exceptions_warning(exception, (
            "Pokud si přejete pokračovat ve změně,"
            "využijte interaktivní režim: ",
            "log-this-config interactive"
        )
    )

def print_value_exceptions_warning(exception):
    """Funkce pro cli výpis chyby hodnoty"""
    print_exceptions_warning(exception, (
            "Pokud si přejete pokračovat ve změně,",
            "vyberte hoodnotu z následující nabídky:",
        )
    )

def print_key_exceptions_warning(exception):
    """Funkce pro cli výpis chyby klíče"""
    print_exceptions_warning(exception, (
            "Pokud si přejete pokračovat ve změně,",
            "vyberte klíč z násedující nabídky:",
        )
    )
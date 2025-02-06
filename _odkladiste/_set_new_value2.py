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

            # Kontrola, zda je používán konfigurační soubor
            if self.config_file:

                # Smazání aktuálního konfiguračního souboru
                delete_config_file(self.config_file_path)

                # Vytvoření nového konfiguračního souboru
                save_config_file(self.config_file_path, self.config)

        # Zachycení výjimky zadání chybného klíče, nebo hodnoty
        # Nebo zadání již existující hodnoty
        except (
                ValidateKeyError,
                ValidateValueError,
                ValueIsAlreadySetError
        ) as e:
            raised_exception = True
            conclusion=(
                "Opakujte zadání, nebo pro změnu konfigurace "
                "využijte interaktivní režim: ",
                "log-this-config interactive"
            )


        # Zachycení výjimky při smazání nebu ukládání konfiguračního souboru
        except (
                DeleteConfigFileError,
                SaveConfigFileError
        ) as e:
            self.config_file = False
            raised_exception = True
            conclusion=(
                "Knihovna poběží i bez konfiguračního souboru."
                "Jediné omezení je že případné změny konfigurace se vám neuloží do příště."
            )

        # Vytvoření informačního logu
        finally:

            # Pokud byla zachycena výjimka
            if raised_exception:
                cli_print(
                    style="warning",
                    info=str(e),
                    detail=e.detail,
                    hint=e.hint,
                    conclusion=conclusion
                )

            # Pokud vše proběhlo v pořádku
            elif value_check:
                cli_print(
                    style="success",
                    info=f"Úspěšné nastavení klíče '{key}' na hodnotu: {value}",
                )




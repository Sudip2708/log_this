from abc import ABC, abstractmethod
from typing import Union, Set, Dict
from pathlib import Path

from ..errors import DeleteConfigFileError, SaveConfigFileError
from ..keys_data_mixins import ConfigKey
from ..utils import save_config_file, delete_config_file, cli_print



class SetNewValueMixin(ABC):

    @property
    @abstractmethod
    def valid_keys(self) -> Set[str]:
        """Property množina s platnými klíči."""
        pass

    @property
    @abstractmethod
    def get_valid_keys_with_descriptions(self) -> str:
        """Vrátí výpis klíčů s krátkým popisem."""
        pass

    @property
    @abstractmethod
    def keys_data(self) -> Dict[str, ConfigKey]:
        """Atribut slovníku s odkazi na třídy jednotlivých klíčů."""
        pass

    @property
    @abstractmethod
    def config_path(self) -> Path:
        """Atribut sonsahujícé cestu ke konfiguračnímu souboru."""
        pass

    @property
    @abstractmethod
    def config(self) -> Dict[str, Union[int, str, bool]]:
        pass


    def set_new_value(
            self,
            key: str,
            value: Union[int, str, bool],
            value_check: bool = False
    ) -> None:

        # Kontrola zda ještě není provedena validace
        if not value_check:
            self.key_value_check(key, value)

        # Uložení změny do konfiguračního slovníku
        self.safe_value_change(key, value)

        # Uložení změny do konfiguračního souboru
        self.rewrite_config_file()


    def key_check(self, key):
        """Kontrola klíče"""
        if key not in self.valid_keys:
            raise KeyError(
                f"\nByl zadán naplatný klíč {key}\n"
                f"{self.get_valid_keys_with_descriptions}"
            )

    def value_check(self, key, value):
        """Kontrola hodnoty"""
        if not self.keys_data[key].validate(value):
            raise ValueError(
                f"\nPro klíč '{key}' byla zadaná neplatná hodnota: {value}\n"
                f"{self.keys_data[key].options}"
            )

    def check_if_value_is_already_set(self, key, value):
        """Kontrola zda se nejedná o již nastavenou hodnotu"""
        if self.config[key] == value:
            raise ValueError(
                f"\nKonfigurační klíč '{key}' je již nastaven na hodnotu {value}\n"
                f"Žádná změna nebyla učiněna."
            )

    def key_value_check(self, key, value):
        """Metoda slučující kontrolu klíče a hodnoty"""
        try:

            # Kontrola klíče
            self.key_check(key)

            # Kontrola hodnoty
            self.value_check(key, value)

            # Kontrola zda se nejedná o již nastavenou hodnotu
            self.check_if_value_is_already_set(key, value)

        except (KeyError, ValueError) as e:
            cli_print('error', str(e))
            print(f"\nInfo: \n"
                  f"  Z výše uvedených důvodů nedošlo k žádné změně.\n"
                  f"  Aplikace poběží se stejným nastavením jako doposud."
                  f"  Pro změnu opakujte volbu s platnými údaji.")

    def rewrite_config_file(self):
        """Metoda uloží změny do konfiguračního souboru"""
        try:
            # Smazání aktuálního konfiguračního souboru
            delete_config_file(self.config_path)

            # Vytvoření nového konfiguračního souboru
            save_config_file(self.config_path, self.config)

            # Oznam o úspěšném uložení souboru
            print(
                "Proběhlo uložení nového nastavení do konfiguračního souboru"
            )

        except (DeleteConfigFileError, SaveConfigFileError) as e:
            print(e)
            print(f"\nInfo: \n"
                  f"  Z výše uvedených důvodů nedošlo k trvalému uložení hodnoty.\n"
                  f"  Konfigurace byla změněna a knihovnu můžete používat.\n"
                  f"  Změna hodnoty se pouze neuložila do konfiguračního souboru,\n"
                  f"  takže při příštím způštění aplikace nebude zohledněna.")

    def safe_value_change(self, key, value):
        """Metoda pro bezpečné uložení změny do konfiguračního slovníku"""

        error_messagge = "Nastavení konfiguračního klíče '{key}' na hodnotu '{value}' se nezdařilo!"

        try:

            # Změna hodnoty
            self.config[key] = value

            # Oznam o úspěšné změny hodnoty
            cli_print(
                "success",
                "Proběhlo nastavení konfiguračního klíče '{key}' na hodnotu: {value}"
            )

        except AttributeError as e:
            cli_print(
                style="critical",
                intro=f"Chyba atributu - {str(e)}",
                info=error_messagge,
                hint=("Knihovna hlásí chybu chybějícího atributu pro konfiguraci.",
                      "Pro nápravu zkuste reinstalovat knihovnu.")
            )
            print(error_msg("Chyba atributu", e))

        except KeyError as e:
            cli_print(
                style="error",
                intro=f"Chyba klíče - {str(e)}",
                info=error_messagge,
                hint=("Došlo k chybnému zadání klíče.",
                      "Seznam klíčů u kterých jde provést konfigurace:",
                      f"{self.valid_keys}",
                      "Můžete opakovat svoji volbu, nebo použít interaktivní režim.")
            )
            print(error_msg("Chyba klíče", e))

        except TypeError as e:
            print(error_msg("Chyba typu", e))

        except Exception as e:
            print(error_msg("Neočekávaná chyba", e))
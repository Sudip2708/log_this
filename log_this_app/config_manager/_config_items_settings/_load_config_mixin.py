from abc import ABC, abstractmethod
from typing import Dict, Union

from abc_helper import abc_property, abc_method



class LoadConfigMixin(ABC):

    # Atribut dokazující na hlavní třídu ConfigManager
    cm = abc_property("cm")

    # Metoda pro navrácení defaultních hodnot
    default_values = abc_method("default_values")


    def load_config(
            self,
    ) -> Dict[str, Union[int, str, bool]]:

        # Pokud se nepoužívá konfigurační soubor
        if not self.cm.config_file_available:

            # Vrácení defaultních hodnot
            return self.default_values()

        # Pokud se používá konfigurační soubor
        try:






            # Pokud se používá konfigurační soubor, ale ještě není vytvořen
            if not self.config_file_path.exists():

                # Volání metody pro vytvoření nového souboru
                save_config_file(self.config_file_path, self.default_values)

                # Vrácení defaultních hodnot
                return self.default_values

            # Pokud se používá konfigurační soubor, ale je již vytvořen
            else:

                # Načtení a validace konfiguračního souboru
                config_dict = load_and_validate_config_file(
                    self.config_file_path)

                # Kontrola zda konfigurační soubor obsahuje všechny klíče
                if set(config_dict.keys()) != set(KEYS_DATA.keys()):
                    # Doplnění chybějícíh klíčů
                    config_dict = merge_with_defaults(config_dict)

                    # Volání funkce pro smazání souboru
                    delete_config_file(self.config_file_path)

                    # Volání metody pro vytvoření nového souboru
                    save_config_file(self.config_file_path, config_dict)

                # Navrácení zkontrolovaného slovníku nebo výjinky
                return config_dict


        except (
                ReadConfigFileError,
                ValidateDictFormatError,
                ValidateKeyError,
                ValidateValueError,
                MergeWithDefaultsError,
                DeleteConfigFileError,
                SaveConfigFileError,
                ConfirmDeleteError
        ) as e:

            # Vytvoření logu popisující výjimku
            cli_print(
                style="warning",
                info=f"Nepovedlo se načíst data z konfiguračního slovníku",
                detail="Knihovnu bude možné normálně používat. \n"
                       "Veškeré změny konfigurace je možné provést, jen nedojde k jejich uložení do konfiguračního souboru. ",
                hint=f"Zde je záznam chyby na které se ověření přístupu na disk zastavilo:\n"
                     f"- {e.message} \n"
                     f"Zde jsou doplňující informace: \n"
                     f"- {e.detail} \n"
                     f"- {e.hint}"
            )

            # Nastavení že se nemá používat konfigurační soubor
            self.config_file = False

            # Navrácení defaultních hodnot
            return self.default_values




from abc import ABC, abstractmethod
from typing import Dict, Union
from pathlib import Path

from ..cli.styler import cli_print
from ..keys import (
    KEYS_DATA,
    default_values
)
from ..utils import (
    load_and_validate_config_file,
    merge_with_defaults,
    delete_config_file,
    save_config_file
)
from ..errors import (
    ValidateKeyError,
    ValidateValueError,
    MergeWithDefaultsError,
    ReadConfigFileError,
    ValidateDictFormatError,
    SaveConfigFileError,
    DeleteConfigFileError,
    ConfirmDeleteError
)


def load_config(
        config_path
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

    # Ověřit že existuje soubor a je možné ho přepsat.
    # Natáhnout a ověřit z něj data

    # Pokud se nepoužívá konfigurační soubor
    if not config_path:

        # Vrácení defaultních hodnot
        return default_values()

    try:

        # Pokud se používá konfigurační soubor, ale ještě není vytvořen
        if not config_path.exists():

            # Volání metody pro vytvoření nového souboru
            save_config_file(config_path, default_values())

            # Vrácení defaultních hodnot
            return default_values()

        # Pokud se používá konfigurační soubor, ale je již vytvořen
        else:

            # Načtení a validace konfiguračního souboru
            config_dict = load_and_validate_config_file(config_path)

            # Kontrola zda konfigurační soubor obsahuje všechny klíče
            if set(config_dict.keys()) != set(KEYS_DATA.keys()):

                # Doplnění chybějícíh klíčů
                config_dict = merge_with_defaults(config_dict)

                # Volání funkce pro smazání souboru
                delete_config_file(config_path)

                # Volání metody pro vytvoření nového souboru
                save_config_file(config_path, config_dict)

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


        # Navrácení defaultních hodnot
        return default_values()




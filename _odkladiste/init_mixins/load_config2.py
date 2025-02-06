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

    config_dict = None

    # Pokud konfigurační soubor již neexistuje
    if config_path.exists():

        try:
            # Načtení a validace konfiguračního souboru
            config_dict = load_and_validate_config_file(config_path)
        except (
            ReadConfigFileError,
            ValidateDictFormatError,
            ValidateKeyError,
            ValidateValueError,
        ) as e:
            print(e)

        try:
            # Kontrola zda konfigurační soubor obsahuje všechny klíče
            if set(config_dict.keys()) != set(KEYS_DATA.keys()):
                # Doplnění chybějícíh klíčů
                config_dict = merge_with_defaults(config_dict)
                # Volání funkce pro smazání souboru
                delete_config_file(config_path)
        except MergeWithDefaultsError as e:
            print(e)
        except DeleteConfigFileError as e:
            print(e)

            # Navrácení zkontrolovaného slovníku nebo výjinky
            return config_dict

        # Pokud konfigurační soubor ještě neexistuje
        else:

            # Volání metody pro vytvoření nového souboru
            save_config_file(config_path, default_values())

            # Navrácení defaultních hodnot
            return default_values()

    # Zachycení všech výjimek které mohu nastat
    # !!!!!!!!!!! Dořešit výjimky a možná větev finally a tam dát i log???
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


        if not (DeleteConfigFileError, ConfirmDeleteError):

            # Volání funkce pro smazání souboru
            delete_config_file(config_path)

            # Volání metody pro vytvoření nového souboru
            save_config_file(config_path, default_values())

        # Vytvoření logu popisující výjimku
        cli_print(
            style="error",
            info=f"{str(e)}",
            detail=f"{e.extra.get('detail')}",
            hint=f"{e.extra.get('hint')}"
        )

        # Navrácení defaultních hodnot
        return default_values()



